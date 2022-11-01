package com.ffs.repository;

import com.ffs.model.Member;
import org.springframework.data.repository.Repository;

import java.util.List;
import java.util.Optional;

public interface MemberRepository extends Repository<Member, Long> {

    Member save(Member member);

    Optional<Member> findMemberById(Long id);

    List<Member> findMemberByName(String name);

    List<Member> findAll();

}
