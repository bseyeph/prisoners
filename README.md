# Prisoners' Dilemma

## Summary

I was given this challenge (along with a handful of other logical challenges) in an interview. The other ones weren't very programmable problems. For example, I was asked some stuff about geography and decision making. You probably could program those things but you'd end up programming longer than it takes to come up with the solution (which is typically the simplest... Occam?).

## Problem

There are 23 prisoners on an island. The prison warden calls everyone together to tell them he's willing to let them all free. Clearly, there's a catch. 

Each day one prisoner will be randomly selected to go into a room with two switches. When they enter, they will flip a switch. They must flip a switch. The warden will let everyone free if at some point someone can tell him with 100% certainty that all the prisoners have entered the room and flipped a switch.

The prisoners have until sundown that day to talk. BUT, after the sun goes down they'll never be able to communicate with eachother ever again in any way. They'll never see eachother. They'll never talk. They can't scratch messages on walls. Nothing. How can a prisoner possibly ever be confident that everyone has entered this room? Oh... if he's wrong then everyone will be executed.

## Caveats

1. Prisoners will never die.
2. There's literally no way for them to communicate.
3. None of the prisoners will need therapy from extreme isolation.

## Solution

Here's what I came up with:

1. They deem one person the "Counter" or leader.
2. They select the left switch as the designation switch.
3. A prisoner enters the room:
  - If prisoner is the leader
    - If the left switch is up; he puts it down and adds to the count
    - If the left switch is down; he switches the right switch
  - If prisoner is not the leader
    - If the left switch is down AND prisoner has never switched it up; he switches it up
    - If the left switch is up OR the prisoner has switched it up; he switches the right switch
    
Following this process, every prisoner will enter at some point and flip the switch up. Eventually, the leader will come in and flip that switch back down and count a prisoner. If that's flawed logic then email me at bseyeph@gmail.com and we can talk that out.

## The Code

This kind of logic is actually pretty simple to code. Create some prisoners, follow those rules, and once count reaches 23 then it's done. I decided to take it a little farther than was requested. I was intrigued by the "the prisoners never die" caveat given to me. How long would this take? How many times would these guys be going into this room? Most importantly, if I'm ever in prison and given this challenge; will my answer work? Could I possibly be alive.

Yup.
