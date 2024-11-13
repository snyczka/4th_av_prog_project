package project2;

import java.time.LocalDateTime;
import java.util.UUID;

public class DeliveryReceip {

    private final UUID receipId;
    private final PackReceip parcel;
    private final Courier courier;
    private LocalDateTime delivery;


    public DeliveryReceip(PackReceip parcel, Courier courier) {
        this.receipId = UUID.randomUUID();
        this.parcel = parcel;
        this.courier = courier;
    }


    public UUID getReceipId() {
        return this.receipId;
    }

    public PackReceip getParcel() {
        return this.parcel;
    }


    public Courier getCourier() {
        return this.courier;
    }


    public LocalDateTime getDelivery() {
        return this.delivery;
    }

    public void setDelivery(LocalDateTime delivery) {
        this.delivery = delivery;
    }


}
