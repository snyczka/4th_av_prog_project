package project2.transactions;


import project2.Admin;
import project2.CheckoutReceip;
import project2.Client;

public class CheckoutTx implements Runnable{

    private final Client user;
    private final Admin admin;
    private final Integer priority;


    public CheckoutTx(Client user, Admin admin, int priority) {
        this.user = user;
        this.admin = admin;
        this.priority = priority;
    }


    public Client getUser() {
        return this.user;
    }


    public Admin getAdmin() {
        return this.admin;
    }

    public Integer getPriority() {
        return this.priority;
    }

    
    @Override
    public void run(){
        synchronized (this.user) {
            if(!this.user.getShoppingCart().isEmpty()){
                float subtotal = (float) this.user.getShoppingCart().stream()
                .map(cart -> (this.admin.getCatalogue().get(cart[0]).getPrice() * (float) cart[1]))
                .reduce(0f, (a, b) -> a + b);
                if(this.user.getWallet() >= subtotal){
                    this.user.setWallet(this.user.getWallet() - subtotal);
                    this.admin.getPackingQueue().put(new CheckoutReceip(this.user.getId(), this.user.getShoppingCart(), this.priority));
                }else{
                    System.out.println(String.format("Failed checkout for '%s' user. Not enough funds.", this.user.getUserName()));
                }
            }else{
                System.out.println(String.format("User %s has nothing in their shopping cart.", this.user.getUserName()));
            }
        }
    }



}
