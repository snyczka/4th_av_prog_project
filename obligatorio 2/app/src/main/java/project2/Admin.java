package project2;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;
import java.util.UUID;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.PriorityBlockingQueue;
import java.util.concurrent.TimeUnit;

import javax.management.openmbean.KeyAlreadyExistsException;

import project2.transactions.CartTx;
import project2.transactions.CheckoutTx;
import project2.transactions.DeliveryTx;
import project2.transactions.PackTx;
import project_exceptions.NoVendorException;

public class Admin {

    private final Hashtable<Integer, Client> users;
    private final List<Integer> userKeys;
    private final Hashtable<Integer, Product> catalogue;
    private final List<Integer> productKeys;
    private final Hashtable<Integer, Seller> vendors;
    private final List<Integer> vendorKeys;
    private final Hashtable<Integer, Courier> couriers;
    private final List<Integer> courierKeys;
    private final ExecutorService cartActivities;
    private final ExecutorService checkoutActivities;
    private final PriorityBlockingQueue<CheckoutReceip> packingQueue;
    private final ExecutorService packagingActivities;
    private final PriorityBlockingQueue<PackReceip> deliveryQueue;
    private final ExecutorService distributionActivities;
    private final Hashtable<UUID, CheckoutReceip> filledCheckouts;
    private final Hashtable<UUID, PackReceip> filledPacks;
    private final Hashtable<UUID, DeliveryReceip> filledDeliveries;




    public Admin(int cartThreads, int checkoutThreads, int packThreads, int distributionThreads) {
        this.users = new Hashtable<>();
        this.userKeys = new ArrayList<>();
        this.catalogue = new Hashtable<>();
        this.productKeys = new ArrayList<>();
        this.vendors = new Hashtable<>();
        this.vendorKeys = new ArrayList<>();
        this.couriers = new Hashtable<>();
        this.courierKeys = new ArrayList<>();
        this.cartActivities = Executors.newFixedThreadPool(cartThreads);
        this.checkoutActivities = Executors.newFixedThreadPool(checkoutThreads);
        this.packingQueue = new PriorityBlockingQueue<>();
        this.packagingActivities = Executors.newFixedThreadPool(packThreads);
        this.deliveryQueue = new PriorityBlockingQueue<>();
        this.distributionActivities = Executors.newFixedThreadPool(distributionThreads);
        this.filledCheckouts = new Hashtable<>();
        this.filledDeliveries = new Hashtable<>();
        this.filledPacks = new Hashtable<>();
    }


    public Admin(Hashtable<Integer,Client> users, List<Integer> userKeys, Hashtable<Integer,Product> catalogue, 
    List<Integer> productKeys, Hashtable<Integer,Seller> vendors, List<Integer> vendorKeys, Hashtable<Integer,Courier> couriers, 
    List<Integer> courierKeys, PriorityBlockingQueue<CheckoutReceip> chekoutQueue, PriorityBlockingQueue<PackReceip> deliveryQueue, 
    int cartThreads, int checkoutThreads, int packThreads, int distributionThreads, Hashtable<UUID, CheckoutReceip> filledCheckouts, 
    Hashtable<UUID, PackReceip> filledPacks, Hashtable<UUID, DeliveryReceip> filledDeliveries) {
        this.users = users;
        this.userKeys = new ArrayList<>();
        this.catalogue = catalogue;
        this.productKeys = new ArrayList<>();
        this.vendors = vendors;
        this.vendorKeys = new ArrayList<>();
        this.couriers = couriers;
        this.courierKeys = new ArrayList<>();
        this.cartActivities = Executors.newFixedThreadPool(cartThreads);
        this.checkoutActivities = Executors.newFixedThreadPool(checkoutThreads);
        this.packingQueue = chekoutQueue;
        this.packagingActivities = Executors.newFixedThreadPool(packThreads);
        this.deliveryQueue = deliveryQueue;
        this.distributionActivities = Executors.newFixedThreadPool(distributionThreads);
        this.filledCheckouts = filledCheckouts;
        this.filledPacks = filledPacks;
        this.filledDeliveries = filledDeliveries;
    }

    public Admin(){
        this.users = new Hashtable<>();
        this.userKeys = new ArrayList<>();
        this.catalogue = new Hashtable<>();
        this.productKeys = new ArrayList<>();
        this.vendors = new Hashtable<>();
        this.vendorKeys = new ArrayList<>();
        this.couriers = new Hashtable<>();
        this.courierKeys = new ArrayList<>();
        this.cartActivities = Executors.newFixedThreadPool(100);
        this.checkoutActivities = Executors.newFixedThreadPool(100);
        this.packingQueue = new PriorityBlockingQueue<>();
        this.packagingActivities = Executors.newFixedThreadPool(100);
        this.deliveryQueue = new PriorityBlockingQueue<>();
        this.distributionActivities = Executors.newFixedThreadPool(100);
        this.filledCheckouts = new Hashtable<>();
        this.filledDeliveries = new Hashtable<>();
        this.filledPacks = new Hashtable<>();
    }


    public List<Integer> getUserKeys() {
        return this.userKeys;
    }

    public List<Integer> getProductKeys() {
        return this.productKeys;
    }

    public List<Integer> getVendorKeys() {
        return this.vendorKeys;
    }

    public List<Integer> getCourierKeys() {
        return this.courierKeys;
    }


    public Hashtable<Integer,Courier> getCouriers() {
        return this.couriers;
    }


    public PriorityBlockingQueue<PackReceip> getDeliveryQueue() {
        return this.deliveryQueue;
    }



    public Hashtable<Integer,Client> getUsers() {
        return this.users;
    }

    public Hashtable<Integer, Product> getCatalogue() {
        return this.catalogue;
    }

    public Hashtable<Integer,Seller> getVendors() {
        return this.vendors;
    }

    public ExecutorService getCartActivities() {
        return this.cartActivities;
    }


    public ExecutorService getCheckoutActivities() {
        return this.checkoutActivities;
    }


    public PriorityBlockingQueue<CheckoutReceip> getPackingQueue() {
        return this.packingQueue;
    }


    public ExecutorService getPackagingActivities() {
        return this.packagingActivities;
    }


    public ExecutorService getDistributionActivities() {
        return this.distributionActivities;
    }


    public Hashtable<UUID,CheckoutReceip> getFilledCheckouts() {
        return this.filledCheckouts;
    }

    public Hashtable<UUID,PackReceip> getFilledPacks() {
        return this.filledPacks;
    }

    public Hashtable<UUID,DeliveryReceip> getFilledDeliveries() {
        return this.filledDeliveries;
    }

    public void addClient(int id, String userName, String email, float wallet, int priorityLevel){
        try {
            if(this.users.containsKey(id)){
                throw new KeyAlreadyExistsException();
            }
            Client success = new Client(id, userName, email, wallet, priorityLevel);
            this.users.put(id, success);
            this.userKeys.add(id);
        } catch (KeyAlreadyExistsException badKey) {

        }
    }

    public void addVendor(int id, String name, String contact){
        try {
            if(this.vendors.containsKey(id)){
                throw new KeyAlreadyExistsException();
            }
            Seller success = new Seller(id, name, contact);
            this.vendors.put(id, success);
            this.vendorKeys.add(id);
        } catch (KeyAlreadyExistsException badKey) {

        }
    }

    public void addProduct(int id, String name, float price, int stock, int vendorId){
        try {
            if(this.catalogue.containsKey(id)){
                throw new KeyAlreadyExistsException();
            }
            if(!this.vendors.containsKey(vendorId)){
                throw new NoVendorException();
            }
            Product success = new Product(id, name, price, stock);
            this.catalogue.put(id, success);
            this.productKeys.add(id);
        } catch(KeyAlreadyExistsException badKey){
            System.out.println("Product already exists.");
        }catch(NoVendorException missingVendorException){
            System.out.println("No vendor for Product.");
        }

    }

    public void addCourier(int id, String name, String contact){
        try {
            if(this.couriers.containsKey(id)){
                throw new KeyAlreadyExistsException();
            }
            Courier success = new Courier(id, name, contact);
            this.couriers.put(id, success);
            this.courierKeys.add(id);
        } catch (KeyAlreadyExistsException badKey) {

        }
    }

    public void buy(Client buyer, Product item, int quantity){
        this.cartActivities.submit(new CartTx(buyer, item, quantity));
    }

    public void buy(Client buyer, Product item){
        this.buy(buyer, item, 1);
    }

    public void confrimSale(Client user){
        this.checkoutActivities.submit(new CheckoutTx(user, this, user.getPriorityLevel()));
    }

    public void confrimEmergencySale(Client user){
        this.checkoutActivities.submit(new CheckoutTx(user, this, 0));
    }

    public void packageNextSale(){
        try {
        this.packagingActivities.submit(new PackTx(this.packingQueue.take(), this));
        } catch (InterruptedException e) {
        }
    }

    public void deliverNextPack(){
        try {
            this.distributionActivities.submit(new DeliveryTx(this.deliveryQueue.take(), this));
        } catch (InterruptedException e) {
        }
    }

    public void ceaseOperations(){
        try {
            this.cartActivities.shutdown();
            this.cartActivities.awaitTermination(5,TimeUnit.SECONDS);
            this.checkoutActivities.shutdown();
            this.checkoutActivities.awaitTermination(5,TimeUnit.SECONDS);
            this.packagingActivities.shutdown();
            this.packagingActivities.awaitTermination(5,TimeUnit.SECONDS);
            this.distributionActivities.shutdown();
            this.distributionActivities.awaitTermination(5,TimeUnit.SECONDS);
        } catch (InterruptedException e) {
        }
    }
}
