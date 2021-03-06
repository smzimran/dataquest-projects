## 1. Introduction ##

# Let's say this is your running history for the past week
# For each day, it records whether or not you ran, and whether or not you were tired
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

# Let's say we want to use Bayes' theorem to calculate the odds that you were tired, given that you ran
# This is P(A)
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B)
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A)
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was tired"])

# Now we can calculate P(A|B)
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran

print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))

## 6. Computing Prediction Error ##

actual = [int(r[1]) for r in test]

from sklearn import metrics

# Generate the ROC curve using scikits-learn
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)

# Measure the area under the curve
# The closer to 1 it is, the "better" the predictions
print("AUC of the predictions: {0}".format(metrics.auc(fpr, tpr)))