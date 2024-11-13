package project2.transactions;

import project2.Admin;
import project2.Courier;
import project2.DeliveryReceip;
import project2.PackReceip;

public class DeliveryTx implements Runnable{

    private final PackReceip parcel;
    private final Admin admin;
    private boolean delivered;


    public DeliveryTx(PackReceip parcel, Admin admin) {
        this.parcel = parcel;
        this.admin = admin;
        this.delivered = false;
    }


    public Admin getAdmin() {
        return this.admin;
    }

    public PackReceip getParcel() {
        return this.parcel;
    }

    public boolean isDelivered() {
        return this.delivered;
    }

    public boolean getDelivered() {
        return this.delivered;
    }

    public void setDelivered(boolean delivered) {
        this.delivered = delivered;
    }

    @Override
    public void run() {
        
        try {
            int posibleCouriers = this.admin.getCouriers().keySet().size();
            int selectedCourierIndex = 0 + (int)(Math.random() * ((posibleCouriers - 0) + 1));
            Courier selectedCourier = this.admin.getCouriers().get(this.admin.getCourierKeys().get(selectedCourierIndex));
            DeliveryReceip receip = new DeliveryReceip(this.parcel, selectedCourier);
            this.admin.getFilledPacks().put(this.parcel.getReceipId(), this.parcel);
            Thread.sleep(1000l + (long)(Math.random() * ((3000l - 1000l) + 1l)));
            this.admin.getFilledDeliveries().put(receip.getReceipId(), receip);
            this.delivered = true;
        } catch (InterruptedException e) {
        }



    }


}
