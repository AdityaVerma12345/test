Hey seniors! this is my first time using git and all, so thnx it is nice to do this whole coding.
<br>It's my first time doing coding for this long and I really enjoyed it.
<br>I took help for AI for this but know full well what each line means and can write most of it without using AI.
<br>if you need here is the conversation from start between me and gpt : https://chatgpt.com/share/6aee0d22-5dc4-83e8-a4b1-220f7a0ce73a, https://chatgpt.com/share/6af00e2e-3bf4-83ee-a064-caf3a2b70ac9, https://chatgpt.com/share/6af00e40-9194-83e8-a3d2-0ff9435c3efa, https://chatgpt.com/share/6af00e52-27b0-83e8-a280-0c70d50129e8 . 

<br>1. Project overview:- It does everything what you have asked for.

<br>2. Technologies Used:- Python 3, heapq — priority queue implementation, json — reading and writing JSON data, datetime — recording request submission times.

<br>3. Structure:- Hi.py is main file and there is README.md and cabs.json for you to input cabs data and save_data.json for updated data to save in to prevent loss of data after quiting.

<br>4. How to run:- load the git repositery on ur computer and then load your own json file if you have then just run it. You will get a menu with options to 

<br>5. Priority Queue Implementation:- I used Heapq for it. By multiplying -1 to the year of the student, then it will make it the more senior the student is less the value it will be so heapq will prioritise senior one. basically used the format (-student.year, student.ride_no, student). In this student.year is used for priority and second priority is given to student.ride_no so that if the year is same then whoever has first requested cab will be prioritised.

<br>6. Time complexity:- for requesting ride request:- nlog(n).
                     for dispatching ride request:- nlog(n).
                     for matching passengers :- nlog(n).

<br>7. Tricky situations:-
<br>i. Half empty cab: the cab will depart with just 1 or 2 students. The students will be remode from waiting queue.
<br>ii. No cabs left: the request of the student will be accepted and will be put in the priority queue and program will indicate that no matching cab available
<br>iii. Same year: bcz the heap stores (-student.year, student.ride_no, student), student of same year who registers first will be prioritise
<br>iv. Lots of students: Adding one student will take log(n) time and 1000 studnets will take 1000log(n) time. Sending of will also take nlog(n) time and findingn open cab will also take nlog(n) time

<br>8. I have'nt used persistence, thing used to save even after quiting yet as I don't know it. Hoping to first study and then implement it. Let's see about that later.