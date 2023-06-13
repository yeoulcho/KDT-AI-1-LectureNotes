package kr.jinho.jinhokim.testCode.account.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
public class AccountRole {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String role;

    @ManyToOne
    @Getter
    private TestAccount account;

    public AccountRole(String role, TestAccount account) {
        this.role = role;
        this.account = account;
    }
}
