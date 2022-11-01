package com.ffs.model;

import com.ffs.model.type.MemberStatus;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDate;
import java.util.List;

@Entity
@Data
@Table(name = "MEMBER")
public class Member {

    @Id @GeneratedValue
    @Column(name="MEMBER_ID")
    private long id;

    @Column(name="LOGIN_ID", length = 16, nullable = false, unique = true)
    private String loginId;

    @Column(name="LOGIN_PASSWORD", length = 32, nullable = false)
    private String loginPassword;

    @Column(name="NAME", length = 8, nullable = false)
    private String name;

    @Column(name="BIRTH", nullable = false)
    private LocalDate birth;

    @Column(name="PHONE_NUMBER", length = 12, nullable = false)
    private String phoneNumber;

    @Enumerated
    @Column(name="STATUS", nullable = false)
    private MemberStatus status;

    @ManyToOne
    @JoinColumn(name = "TRAINER_ID")
    private Trainer trainer;

    @OneToOne
    @JoinColumn(name="MEMBERSHIP_ID")
    private Membership membership;

    @OneToMany(mappedBy = "member")
    private List<Payment> paymentList;

    @OneToMany(mappedBy = "member")
    private List<Lesson> lessonList;
}
