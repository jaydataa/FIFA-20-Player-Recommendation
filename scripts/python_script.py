# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
def load_data():
    # Update the file path as per your project directory
    players_df = pd.read_csv('players.csv')
    teams_df = pd.read_csv('teams.csv')
    return players_df, teams_df

# Data cleaning function
def clean_data(df):
    # Removing irrelevant columns and handling missing values
    df = df[['sofifa_id', 'short_name', 'long_name', 'age', 'dob', 'height_cm', 'weight_kg', 'nationality', 
             'club', 'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions', 'preferred_foot', 
             'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 
             'gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning']]

    # Fill missing values or drop rows with missing data
    df = df.dropna()

    return df

# Visualisation functions
def plot_player_distribution(df):
    # Distribution of Player Overall Ratings
    plt.figure(figsize=(10, 6))
    sns.histplot(df['overall'], kde=True, color='skyblue')
    plt.title('Distribution of Player Overall Ratings')
    plt.xlabel('Overall Rating')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('player_overall_distribution.png')
    plt.show()

def plot_top_players(df):
    # Top 10 Players by Overall Rating
    top_players = df[['short_name', 'overall']].sort_values(by='overall', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='overall', y='short_name', data=top_players, palette='viridis')
    plt.title('Top 10 Players by Overall Rating')
    plt.xlabel('Overall Rating')
    plt.ylabel('Player Name')
    plt.grid(True)
    plt.savefig('top_10_players_by_rating.png')
    plt.show()

def plot_player_attributes_heatmap(df):
    # Heatmap of Player Attributes (Correlation)
    attributes = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[attributes].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of Player Attributes')
    plt.tight_layout()
    plt.savefig('player_attributes_heatmap.png')
    plt.show()

# Recommendation Engine
def recommend_similar_players(df, player_name):
    # Filter out the player from the dataset
    player = df[df['short_name'] == player_name].iloc[0]

    # Select relevant features for similarity calculation
    features = ['overall', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
    player_features = player[features].values.reshape(1, -1)

    # Calculate cosine similarity for all players based on selected features
    similarity_scores = cosine_similarity(player_features, df[features])

    # Add the similarity scores to the dataframe and sort by similarity
    df['similarity_score'] = similarity_scores.flatten()
    similar_players = df[['short_name', 'similarity_score']].sort_values(by='similarity_score', ascending=False)

    # Exclude the original player from the recommendation list and return the top 5 similar players
    similar_players = similar_players[similar_players['short_name'] != player_name].head(5)
    return similar_players

# Main function to execute the steps
def main():
    # Load and clean data
    players_df, teams_df = load_data()
    players_df = clean_data(players_df)

    # Generate visualisations
    plot_player_distribution(players_df)
    plot_top_players(players_df)
    plot_player_attributes_heatmap(players_df)

    # Recommend similar players
    player_name = "Lionel Messi"  # Example player
    similar_players = recommend_similar_players(players_df, player_name)
    print(f"Top 5 similar players to {player_name}:")
    print(similar_players)

if __name__ == '__main__':
    main()
