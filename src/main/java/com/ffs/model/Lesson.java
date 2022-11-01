package com.ffs.model;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalTime;

@Data
@Entity
@Table(name = "LESSON")
public class Lesson {

    @Id @GeneratedValue
    @Column(name = "LESSON_ID")
    private long id;

    @ManyToOne
    @JoinColumn(name = "MEMBER_ID")
    private Member member;

    @ManyToOne
    @JoinColumn(name = "TRAINER_ID")
    private Trainer trainer;

    @Column(name = "LESSON_DATE")
    private LocalDate lessonDate;

    @Column(name = "LESSON_TIME")
    private LocalTime lessonTime;


    private String note;
}
