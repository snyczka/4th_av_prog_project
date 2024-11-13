package project2;

import java.util.Objects;

public class Courier {

    private final Integer courierId;
    private final String courierName;
    private final String courierContact;


    public Courier(Integer courierId, String courierName, String courierContact) {
        this.courierId = courierId;
        this.courierName = courierName;
        this.courierContact = courierContact;
    }

    public Integer getCourierId() {
        return this.courierId;
    }

    public String getCourierName() {
        return this.courierName;
    }

    public String getCourierContact() {
        return this.courierContact;
    }


    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Courier)) {
            return false;
        }
        Courier courier = (Courier) o;
        return Objects.equals(courierId, courier.courierId) && Objects.equals(courierName, courier.courierName) && Objects.equals(courierContact, courier.courierContact);
    }

    @Override
    public int hashCode() {
        return Objects.hash(courierId, courierName, courierContact);
    }

}
