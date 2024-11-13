package project2.transactions;


import project2.Client;
import project2.Product;

public class CartTx implements Runnable{

    private final  Client buyer;
    private final  Product item;
    private final  int unitsBought;
    


    public CartTx(Client buyer, Product item, int unitsBought) {
        this.buyer = buyer;
        this.item = item;
        this.unitsBought = unitsBought;
    }

    private void addToCart(){
        synchronized(this.item) {
            if(this.item.getStock() >= this.unitsBought){
                this.item.setStock(this.item.getStock() - this.unitsBought);
                Integer[] purchase = {this.item.getId(), this.unitsBought};
                this.buyer.getShoppingCart().add(purchase);
            }else{
                System.out.println(String.format("Insufficient Stock of %s for user: %s", 
                this.item.getName(), this.buyer.getUserName()));
            }
        }
        
        
        
       

    }
    
    @Override
    public void run() {
        this.addToCart();
    
    }

    


}
