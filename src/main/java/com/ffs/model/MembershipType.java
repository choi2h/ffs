package com.ffs.model;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "MEMBERSIP_TYPE")
public class MembershipType {

    @Id @GeneratedValue
    @Column(name="MEMBERSHIP_TYPE_ID")
    private int id;

    @Column(name="NAME", length = 100, nullable = false)
    private String name;
}
