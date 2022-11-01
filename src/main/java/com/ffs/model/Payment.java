package com.ffs.model;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDateTime;

@Data
@Entity
public class Payment {
    @Id @GeneratedValue
    @Column(name="PAYMENT_ID")
    private String id;

    @ManyToOne
    @JoinColumn(name = "payment")
    private Member member;

    @Column(name = "PAY_DATE", nullable = false)
    private LocalDateTime payDate;

    @Column(name = "AMOUNT", nullable = false)
    private int amount;

    @OneToOne
    @JoinColumn(name="MEMBERSIHIP_TYPE_ID")
    private MembershipType membershipType;
}
