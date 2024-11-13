package project2;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

public class PackReceip implements Comparable<PackReceip>{

    private final UUID receipId;
    private final Integer userId;
    private final List<Integer[]> parcel;
    private final LocalDateTime packIssued;
    private final Integer priority;


    public PackReceip(Integer userId, List<Integer[]> parcel, LocalDateTime packIssued, Integer priority) {
        this.receipId = UUID.randomUUID();
        this.userId = userId;
        this.parcel = parcel;
        this.packIssued = packIssued;
        this.priority = priority;
    }


    public Integer getPriority() {
        return this.priority;
    }

    
    public UUID getReceipId() {
        return this.receipId;
    }

    public Integer getUserId() {
        return this.userId;
    }

    public List<Integer[]> getParcel() {
        return this.parcel;
    }

    public LocalDateTime getPackIssued() {
        return this.packIssued;
    }

    @Override
    public int compareTo(PackReceip o) {
        return Integer.compare(this.priority, o.getPriority());
    }


}
