package project2;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Seller {

    private final int id;
    private String name;
    private String contact;
    private List<Product> offerings;
    

    public Seller(int id, String name, String contact) {
        this.id = id;
        this.name = name;
        this.contact = contact;
        this.offerings = new ArrayList<>();
    }



    public int getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getContact() {
        return this.contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public List<Product> getOfferings() {
        return this.offerings;
    }

    public void setOfferings(List<Product> offerings) {
        this.offerings = offerings;
    }


    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Seller)) {
            return false;
        }
        Seller seller = (Seller) o;
        return id == seller.id && Objects.equals(name, seller.name) && Objects.equals(contact, seller.contact) && Objects.equals(offerings, seller.offerings);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id);
    }

    

}
