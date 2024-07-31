#include <iostream>
#include <stdio.h>
#include <string.h>

void func() {
    //static으로 선언된 값은 처음 한번만 초기화가되기 때문에 다시 호출되어도 초기화는 되지 않는다.
    //static 변수들은 프로그램이 종료도리 때까지 소멸되지 않기 때문에
    //func이 여러번 호출되는 경우에도 초기화는 한 번만 수행한다.
    static int a = 3;

    a = a+1;
    printf("%d\n",a);
}
void ex2() {
    //포멧 스트링 종류
/*  %C 문자
 *  %S String
 *  %u 부호없는 10진수
 *  %d 10진수
 *  %o 8진수
 *  %x 16진수
 */
 //시프트 연산
    int x = 11;
    int result = x<<3; //왼쪽으로 3비트 추가 즉 1011->1011000
    printf("%d",result);
    x = 11;
    result = x>>1; //오른쪽으로 1비트 없앰 1011 -> 101
    printf("%d",result);
    //비트 연산
    //&, |, ^, ~ ~는 not임 (완전반전)

}
void ex3() {
    // switch 문
    int score = 101;
    switch (score/10) { //핵심 포인트는 해당 조건이 있을 떄 그 케이스 문으로 가고 break이 있을 때까지 내려간다.
        case 10 :
            case 9:
            printf("A");
        break;
    }
}
void ex4() {
    //배열
    int a[3] = {1,2}; //1,2,0저장된다.
    for (auto a1: a) {
        // printf("%d\n",a1);
    }
    int a2[3][4] = {1,2,3,4,5};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 4; ++j) {
            printf("%d",a2[i][j]);
        }
        printf("\n");
    }
    //배열 출력
    char char_string [8] = "HELLO";
    printf("%s\n",char_string);
    printf("%s\n",char_string+1);
    printf("%s\n",char_string+2);
    printf("%s\n",char_string+3); // 3번째부터 출발 LO 출력됨

    //배열 출력에서 위에 처럼 글을 읽다 Null을 발견하면 종료하면서 문자를 출력한다.
    char_string[4] = NULL;
    printf("%s\n",char_string);
}
void structure_test() {
    //구조체란 사용자가 기본 자료형을 가지고 새롭게 정의할 수 있는 사용자 정의 자료형이다.
    //자바에서 생성자 역할
    char gender;
    int age ;

}
void functions_test() {
    //Call by Value ;
    //변수의 값을 넘겨주고, 이 값은 새로운 공간에 할당되어 사용되는 방식
    //기존 값이 변경되지 않는다.
    //Call by Reference ;
    //변수의 값이 아닌 변수가 사용 중인 메모리 공간의 주소를 넘겨주는 방식
    //실 매개 변수의 주소를 형식 매개 변수로 보냄.
}
void standardFunctions(){
    //strcpy
    char a[20] = "Heelo";
    char b[10] = "inho";
    strcpy(a,b); //a를 b로 바꾼다.
    printf("%s %s\n",a,b);
    //strcat
    //이어붙이는 것
    //strcmp : 아스키 코드값을 통한 문자열의 대소를 비교한다 .
    //strncmp : maxlen 길이를 줘서 그 값만큼만 비교한다.
    char s[10] = "ASDF";
    char s1[20] = "QWER";
    int c  =strcmp(s,s1); //같으면 0, 앞에 친구가 뒤에 친구보다 작으면 -1
    int c1 = strncmp(s,s1,1);
    //strlen 문자열의 길이를 알려주는 함수
    char test[20] = "ASDF";
    c = strlen(test);
    printf("%d",c);
}
void pointer() {
    int a = 10;
    int *b = &a;
    printf("%d %d %d \n",a,*b,*(&a));
    printf("%d %d %d %d", a, &a, b, *(&b));
}
void pointer1() {
    int num[3]  = {1,2,3};
    // printf("%d",num);

}
struct struct_test {
    char *name;
    int age;
} st;
int main() {
    // #1
    // func();
    // func();
    pointer1();
    return 0;
}
