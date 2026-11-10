Hey seniors! this is my first time using git and all, so thnx it is nice to do this whole coding.
<br>It's my first time doing coding for this long and I really enjoyed it.
<br>I took help for AI for this but know full well what each line means and can write most of it without using AI.

<br>1. Project overview:- It does everything what you have asked for.

<br>2. Technologies Used:- Python 3, heapq — priority queue implementation, json — reading and writing JSON data, datetime — recording request submission times.

<br>3. Structure:- Hi.py is main file and there is README.md and cabs.json for you to input cabs data and save_data.json for updated data to save in to prevent loss of data after quiting.

<br>4. How to run:- load the git repositery on ur computer and then configure your own cabs.json file if you have then just run it. You will be presented with a menu with 7 options in it: 1. To add a ride request, 2. to view waiting students, 3. to view all cabs, 4. to find passenger matche, 5. to dispatch a cab, 6. to save and quit and 7. ot quit the program.

<br>5. Priority Queue Implementation:- I used Heapq for it. By multiplying -1 to the year of the student, then it will make it the more senior the student is less the value it will be so heapq will prioritise senior one. basically used the format (-student.year, student.ride_no, student). In this student.year is used for priority and second priority is given to student.ride_no so that if the year is same then whoever has first requested cab will be prioritised.

<br>6. Time complexity:- for requesting ride request:- nlog(n).
                     for dispatching ride request:- nlog(n).
                     for matching passengers :- nlog(n).

<br>7. Tricky situations:-
<br>i. Half empty cab: the cab will depart with just 1 or 2 students. The students will be remode from waiting queue.
<br>ii. No cabs left: the request of the student will be accepted and will be put in the priority queue and program will indicate that no matching cab available
<br>iii. Same year: bcz the heap stores (-student.year, student.ride_no, student), student of same year who registers first will be prioritise
<br>iv. Lots of students: Adding one student will take log(n) time and 1000 studnets will take 1000log(n) time. Sending of will also take nlog(n) time and findingn open cab will also take nlog(n) time
<br>v. There was another situation, suppose there are two cabs going to same place at same time but first one with 3 seat capacity and second one with 4 seat capacity. My program was giving priority to first one as it was written first, even though there are 4 student waiting for that. So I changed it to give priority to max occupying student. Well i took a bit of help of AI in this too

<br>8. I have'nt used persistence, thing used to save even after quiting yet as I don't know it. Hoping to first study and then implement it. Let's see about that later.

<br> I'm have now implimented the bonus part where it gets saved.
<br> Expected structure in cabs.jsom:-
    example:
        {
        "driver_name": "Name",
        "seats": 2,
        "destination": "Delhi",
        "time_slot": "Morning"
    }
<br> destination can only be 'delhi' or 'jaipur'.
<br> time slot can only be 'morning', 'afternoon', 'evening' or 'night'.
<br>Thank you :)