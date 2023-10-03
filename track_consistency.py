from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot
from consistency_data import SHAUNTAL_CONSISTENCY_TUPLES

shauntal_consistency = calculate_consistency(SHAUNTAL_CONSISTENCY_TUPLES)
save_plot("Shauntal Consistency Score", shauntal_consistency, "shauntal_score_plot.png")