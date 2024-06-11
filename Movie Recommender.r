# CSE310-movies-recommand.r


# Overview

{this is a movie recommendation system in R. it uses a dataset called "metadata" from imdb database. the csv file is here:https://drive.google.com/file/d/1lpECPf6q73JrogjbwkBRBM8Uxprq2--Q/view?usp=sharing }

{the purpose for this software is to get a brief understanding of R and take advantage of the dataset provided to find the movie we may like.}

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running and a walkthrough of the code. Focus should be on sharing what you learned about the language syntax.}

[Software Demo Video]: https://youtu.be/cKGD307DXaE 

# Development Environment

{I used  one of the csv file from imdb's open database.I also intsalled the R extension in vs code studio, but ended up not using it. Eventually I decided to use Colab since it's associated with the google drive account, which allows me to upload the csv file. }



# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- ask user for more detailed proference, for example, rating, length.etc
- merged with other dataset like keywords, and ratings
- use a more comlicated model to train the data such as Matrix factorization


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Read the dataset
metadata <- read.csv("movies_metadata.csv", stringsAsFactors = FALSE)

# a function to clean up the language column from JSON-like strings to a more clear version
extract_language <- function(column_str)
{
  # Extract language names
  # the original format example: [{'iso_639_1': 'en', 'name': 'English'}]
  language_name <- gsub("\\{'iso_639_1': '\\w+', 'name': '(.*?)'\\}", "\\1", column_str, perl = TRUE)

  return(language_name)
}

# Apply the function to the spoken_languages column
metadata$spoken_languages <- sapply(metadata$spoken_languages, extract_language)


# a function to clean up the gengre column
extract_genres <- function(column_str) {
  # Extract genre names using regular expression
  genre_names <- gsub("\\{'id': \\d+, 'name': '(.*?)'\\}", "\\1", column_str, perl = TRUE)

  # Collapse multiple genre names into a single string
  genre_names <- toString(genre_names)

  return(genre_names)
}

# Apply the function to the genres column
metadata$genres <- sapply(metadata$genres, extract_genres)



# only keep the columns  that we need from metadata file
columns_to_keep <- c("adult", "genres", "id", "original_language",
                     "original_title", "overview", "popularity", "release_date", "runtime",
                     "spoken_languages", "tagline", "title", "vote_average", "vote_count")

# Subset the metadata dataframe to include only the specified columns
metadata_subset <- metadata[columns_to_keep]

# print out the first several rows to show the format
head(metadata_subset)




# a function to display available genres
display_available_genres <- function(metadata_subset) 
{
  # Extract unique genres
  unique_genres_combined <- unique(unlist(strsplit(metadata_subset$genres, ", ")))
  unique_genres_combined <- gsub("\\[|\\]", "", unique_genres_combined)
  unique_genres_combined <- unique(unlist(strsplit(unique_genres_combined, ", ")))

  cat("Available genres:", "\n")
  cat(unique_genres_combined, sep = ", ", "\n\n")
}

# Display available genres
  display_available_genres(metadata_subset)


# a function to recommend a movie based on user's answer of preference
recommend_movie <- function(metadata_subset, preferred_genre, preference, adult_preference, popularity_preference) 
{
  # Filter metadata_subset based on preferred genre
  selected_movies <- metadata_subset[grep(preferred_genre, metadata_subset$genres, ignore.case = TRUE), ]

  # Filter selected movies based on preference for old or new movies
  if (preference == "old") 
  {
    selected_movies <- selected_movies[selected_movies$release_date < "2000-01-01", ]   # define the released date before 2000 as old
  } 
  else if (preference == "new") 
  {
    selected_movies <- selected_movies[selected_movies$release_date >= "2000-01-01", ]
  }

  # Filter selected movies based on  preference for movies only for adults
  if (adult_preference == "yes") 
  {
    selected_movies <- selected_movies[selected_movies$adult == "True", ]
  }

  # Filter selected movies based on preference for popularity
  if (popularity_preference == "yes") 
  {
    selected_movies <- selected_movies[selected_movies$popularity >= median(selected_movies$popularity, na.rm = TRUE), ]   # use media  to define if it's popular or not
  }

  # Select a random movie from the filtered subset
  random_index <- sample(nrow(selected_movies), 1)
  recommended_movie <- selected_movies[random_index, ]

  return(recommended_movie)
}

# a function to ask user for preference
ask_and_recommend_movie <- function(metadata_subset) 
{
  # ask user preferred genre
  preferred_genre <- readline(prompt = "Enter your preferred genre: ")

  # ask user's preference for old or new movies
  preference <- readline(prompt = "Do you prefer old movies or new movies? (Enter 'old' or 'new'): ")

  # ask user to enter preference for movies only for adults
  adult_preference <- readline(prompt = "Are you looking for movies only for adults? (Enter 'yes' or 'no'): ")

  # ask user preference for populararity
  popularity_preference <- readline(prompt = "Do you care about the popularity of the movie? (Enter 'yes' or 'no'): ")

  # Recommend movie based on user's preferrence
  recommended_movie <- recommend_movie(metadata_subset, preferred_genre, preference, adult_preference, popularity_preference)

  # Show recommended movie
  cat("\nRecommended Movie:", "\n")
  cat("Title:", recommended_movie$title, "\n")
  cat("Overview:", recommended_movie$overview, "\n")
}

# call the function
ask_and_recommend_movie(metadata_subset)

