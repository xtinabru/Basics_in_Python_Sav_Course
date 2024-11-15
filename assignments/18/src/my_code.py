"""
18

Create a software that computes total point in ski jump competition. The software prints length of the jump and total points to screen. 

Input data is asked in following order:
1) Jump length, resolution 0.5m.
2) Five style points, 0-20, resolution 0.5 points. The highest and lowest style scores are disregarded, with the remaining three scores added to the distance score.

Example on style points:
- Judges gives style points: 18, 19.5, 17.5, 18.5, 18 
- style_points=18+18+18.5   (19.5 and 17.5 are not counted)

K-point of the hill is 90 meters, define global variable K_point=90.


total_points=(length-K_point)*1.8 + 60 + style_points


Implement following functions:

ask_jump_length() - Asks length of the jump and returns the length as float.
ask_style_points() - Asks all 5 style points and returns list containg points given by judges.
compute_points(length, all_style_points_list) - Returns total points of the jump. all_style_points_list is a list containing all 5 style points 

Example 1:
Length : 120
Judge 1: 14
Judge 2: 1
Judge 3: 17
Judge 4: 20
Judge 5: 17.5
120.0 162.5


Example 2:
Length : 65
Judge 1: 2
Judge 2: 3
Judge 3: 1
Judge 4: 2.5
Judge 5: 20
65.0 22.5
"""
#Write functions and define global variables here!

    
if __name__ == "__main__":
    #Write main program below this line


