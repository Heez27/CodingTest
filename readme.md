# 코딩테스트

### ch1. 


### ch2. 


### ch3. 그리디

##### 1) 그리디 Greedy 알고리즘(욕심쟁이 알고리즘): 현재 상황에서 지금 당장 좋은 것만 고르는 방법
   사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형
   
 
    Q1) 당신은 편의점의 계산을 도와주는 점원이다. 
       카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
       손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러줘야 할 동전의 최소 개수를 구하라.
       단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
       
##### 2) 하지만, 가장 큰 화폐 단위가 나머지 화폐의 배수가 아니라면, 그리디 알고리즘으로 해결할 수 없다. 
 예를 들어, 화폐 단위가 500원, 400원, 100원 인 경우는, <br>
 그리디 방법: 800원 = 500원 + 100원 + 100원 + 100원 (총 4개) <br>
 최적의 방법: 800원 = 400원 + 400원 (총 2개)


##### 3) 큰 수의 법칙: 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것
 예1) [2, 4, 5, 4, 6]이라는 배열이 있고, M = 8, K = 3일때,  <br>
 8개의 숫자를 더하고, 특정한 인덱스의 수가 연속해서 3번까지만 더해질 수 있으므로, <br>
 최적의 방법: 6+6+6+5+ 6+6+6+5 = 46
       
 예2) [3, 4, 3, 4, 3]이라는 배열이 있고, M = 7, K = 2일때,  <br>
 7개의 숫자를 더하고, 특정한 인덱스의 수가 연속해서 2번까지만 더해질 수 있으므로, <br>
 최적의 방법: 4+4+ 4+4+ 4+4+ 4 = 28 (인덱스가 다른 4를 2번씩 더함)
 
 
    Q2) 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 연속으로 더할 수 있는 횟수 K가 주어질 때, 위 큰 수의 법칙에 따른 결과를 출력하시오.
       입력조건: 1. 먼저, N, M, K을 받는다. 단, K<=M이다.
               2. N개의 자연수의 입력을 받는다. 
       출력조건: 위의 큰 수의 법칙에 따라 더해진 답을 출력한다. 
 
 

### ch4. 구현

### ch5. DFS/BFS

### ch6. 정렬

### ch7. 이진 탐색

### ch8. 다이나믹 프로그래밍

### ch9. 최단 경로

### ch10. 그래프 이론

