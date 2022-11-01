package com.ffs.repository;

import com.ffs.model.Member;
import com.ffs.model.type.MemberStatus;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDate;
import java.util.Optional;

@SpringBootTest
class MemberRepositoryTest {

    @Autowired
    MemberRepository memberRepository;

    @Test
    void saveMemberTest() {
        Member member = getMember("hwa");
        Member saveMember  = memberRepository.save(member);

        Optional<Member> findMember = memberRepository.findMemberById(saveMember.getId());

        Assertions.assertEquals(member.getName(), findMember.get().getName());
    }

    private Member getMember(String name) {
        Member member = new Member();
        member.setLoginId("hi");
        member.setLoginPassword("pass");
        member.setBirth(LocalDate.now());
        member.setName(name);
        member.setStatus(MemberStatus.ING);
        member.setPhoneNumber("01022223333");

        return member;
    }

}