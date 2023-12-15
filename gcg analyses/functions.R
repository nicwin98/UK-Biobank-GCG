## Create function to make a new_col_name = 1 if an individual has a specific ICD10.
## If multiple search_pattern, provide as a vector c("x", "y")

find_ICD10_filter <- function(data, search_pattern, new_col_name) {
    # Get the names of columns that match the pattern
    column_names <- names(data)
    matching_columns <- grep("^diagnoses_icd10_f41270_0_\\d+$", column_names)

    # Create a logical vector indicating if the search_pattern is contained in each row
    found_in_rows <- apply(data[, ..matching_columns, with = FALSE], 1, function(row) {
        any(grepl(paste(search_pattern, collapse = "|"), as.character(row)))
    })

    # Add the "search_result" column with 1 if a match is found in any column, 0 otherwise
    data[[new_col_name]] <- as.integer(found_in_rows)

    return(data)
}


## Create funktion to make a new_col_name = 1 if an individual has a specific drug code. If multiple search_integers, provide as a vector c(x, y)

find_drug_filter <- function(data, search_integers, new_col_name) {
    # Define the pattern to match column names
    pattern <- "^treatmentmedication_code_f20003_\\d+_\\d+$"

    # Get the names of columns that match the pattern
    column_names <- names(data)
    matching_columns <- column_names[grep(pattern, column_names)]

    # Create a logical vector indicating if any of the search_integers appear in each row
    found_in_rows <- apply(data[, ..matching_columns, with = FALSE], 1, function(row) any(search_integers %in% as.integer(row)))

    # Add the "search_result" column with 1 if any search_integer is found in any row, 0 otherwise
    data[[new_col_name]] <- as.integer(found_in_rows)

    return(data)
}

