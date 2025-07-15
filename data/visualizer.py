import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def __init__(self, moral_values, decision_log):
        self.moral_values = moral_values
        self.decision_log = decision_log
        
    def plot_mvi(self):
        data = []
        for trait, counts in self.moral_values.items():
            total = counts["saves"] + counts["sacrificed"]
            mvi = counts["saves"] / total if total else 0.5
            data.append((trait, counts["saves"], counts["sacrificed"], mvi))
            
        df = pd.DataFrame(data, columns=["Trait", "Saved", "Sacrificed", "MVI"])
        df = df.sort_values("MVI", ascending=False)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x="Trait", y="MVI", palette="coolwarm")
        plt.xticks(rotation=45, ha='right')
        plt.title("Moral Value Index (MVI) per Trait")
        plt.tight_layout()
        plt.show()
        
    def plot_decision_distribution(self):
        choices = [log["gpt_choice"] for log in self.decision_log]
        count = pd.Series(choices).value_counts().sort_index()
        
        plt.figure(figsize=(6, 4))
        count.plot(kind="bar", color=["#2b83ba", "#fdae61"])
        plt.title("GPT's Decisions Distribution")
        plt.xlabel("Track Chosen")
        plt.ylabel("Number of Times")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
        
    def show_all(self):
        self.plot_mvi()
        self.plot_decision_distribution()