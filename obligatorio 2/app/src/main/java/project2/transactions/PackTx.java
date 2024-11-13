package project2.transactions;

import java.time.LocalDateTime;

import project2.Admin;
import project2.CheckoutReceip;
import project2.PackReceip;

public class PackTx implements Runnable{

    private final CheckoutReceip orderToPack;
    private final Admin admin;


    public PackTx(CheckoutReceip orderToPack, Admin admin) {
        this.orderToPack = orderToPack;
        this.admin = admin;
    }


    public CheckoutReceip getOrderToPack() {
        return this.orderToPack;
    }

    public Admin getAdmin() {
        return this.admin;
    }

    
    @Override
    public void run() {
        try {
            Thread.sleep(1000l + (long)(Math.random() * ((3000l - 1000l) + 1l)));
            LocalDateTime timeOfPack = LocalDateTime.now();
            PackReceip receip = new PackReceip(this.orderToPack.getUserId(), 
            this.orderToPack.getShoppingCart(), timeOfPack, this.getOrderToPack().getPriority());
            this.admin.getDeliveryQueue().put(receip);
            this.admin.getFilledCheckouts().put(this.orderToPack.getReceipId(), this.orderToPack);
        } catch (InterruptedException e) {
        }


    }

    

}
