package com.ffs.model;

import com.ffs.config.converter.BooleanToYNConverter;
import lombok.Data;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Data
@Table(name = "MEMBERSHIP")
public class Membership {

    @Id @GeneratedValue
    @Column(name = "MEMBERSHIP_ID")
    private String MembershipId;

    @Convert(converter = BooleanToYNConverter.class)
    @Column(name="IS_PT", nullable = false)
    private boolean isPT;

    @Column(name = "START_DATE", nullable = false)
    private LocalDate startDate;

    @Column(name = "END_DATE", nullable = false)
    private LocalDate endDate;

    @OneToOne(mappedBy = "membership")
    private Member member;
}
