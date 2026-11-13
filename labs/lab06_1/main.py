# Starting file for LAB 6-1
# Include your course number, student first and last name, and date in the comment header
# CS31 Isabella Garcia 11/12/26
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = [] #this code will initalize an empty list
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100: #didn't raise to 120 like in video bcs has to do w test sscores now, not ages
               scores.append(score) #adding value to list w/ append method, name of list, append, value
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total = 0 #initalizing variable, starting "for" loop
    for score in scores:
        total += score

    average = round(total / len(scores)) #length of scores will tell how many items are in there
    
    low_score = min(scores)
    high_score = max(scores) #how to get min and max values
    median_index = len(scores) // 2
    if len(scores) % 2 == 1: #this means if it is odd, % is modules
        median_score = scores[median_index] 
    else: #for if it's even
        middle1 = scores[median_index]
        middle2 = scores[median_index - 1] #find the item of the one next to it
        median_score = (middle1 + middle2) / 2

                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores) #change all to scores to account for list, old variables don't exist
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

