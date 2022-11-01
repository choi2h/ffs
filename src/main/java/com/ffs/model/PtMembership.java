package com.ffs.model;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDateTime;

@Data
public class PtMembership {

    @Id @GeneratedValue
    @Column(name = "PT_MEMBERSHIP_ID")
    private long id;

    @ManyToOne
    @JoinColumn(name = "MEMBERSHIP_ID")
    private String MembershipId;

    @Column(name = "PAY_DATE", nullable = false)
    private LocalDateTime payDate;

    @Column(name = "TOTAL_LESSON_COUNT", nullable = false)
    private int totalLessonCount;

    @Column(name = "USE_LESSON_COUNT", nullable = false)
    private int useLessonCount;

    @Column(name = "PRICE_PER_LESSON", nullable = false)
    private int pricePerLesson;
}
