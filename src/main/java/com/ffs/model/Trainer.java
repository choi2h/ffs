package com.ffs.model;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Data
@Entity
public class Trainer {

    @Id @GeneratedValue
    @Column(name = "TRAINER_ID")
    private Long id;

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

    @Column(name = "WORKING_START_DATE", nullable = false)
    private LocalDate workingStartDate;

    @Column(name = "WORKING_START_TIME", nullable = false)
    private LocalDateTime workingStartTime;

    @Column(name = "WORKING_END_TIME", nullable = false)
    private LocalDateTime workingEndTime;

    @OneToMany(mappedBy = "trainer")
    private List<Member> memberList;

    @OneToMany(mappedBy = "trainer")
    private List<Lesson> lessonList;
}
