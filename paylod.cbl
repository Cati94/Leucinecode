




*A
B 
IDENTIFICATION DIVISION.
PROGRAM-ID PAYROLOO.
DATA DIVISION.
WORKING-STORAGE SECTION.
******** Variables for the report
?? WHO PICX(15).
?? WHERE PICX(20).
?? WHY PICX(30).
?? RATE PIC9(3).
?? HOURS PIC9(3).
?? GROSS-PAY PIC9(5).

       PROCEDURE DIVISION.
********** COBOL MOVE statements - Literal text to variables
MOVE               "Captain Cobol" TO WHO.
MOVE               "San Jose, California" TO WHERE.
MOVE               "Learn to be a COBOL expert" TO WHY.
MOVE               19 TO HOURS.
MOVE               23 TO RATE.

************Calculation using COMPUTE reserved word verb
COMPUTE GROSS-PAY = HOURS * RATE.

************DISPLAY statements       
DISPLAY "Name:"WHO.
DISPLAY "Location:" WHERE.
DISPLAY "Reason:" WHY.
DISPLAY "Hours Worked:" HOURS.
DISPLAY "Hour Ly Rate: " RATE.
DISPLAY "Gross Pay: " GROSS-PAY.
DISPLAY WHY "from " WHO.
GOBACK.    