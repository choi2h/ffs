package com.ffs.model.type;


public enum MemberStatus {
    ING(1), PAUSE(2), END(5);

    private int id;

    MemberStatus(int id) {
        this.id = id;
    }

    public MemberStatus getMemberStatusById(int id) {
        MemberStatus result = MemberStatus.ING;

        MemberStatus[] statusList = MemberStatus.values();
        for(MemberStatus status : statusList) {
            if(id == status.id) {
                result = status;
                break;
            }
        }
        return result;
    }
}
