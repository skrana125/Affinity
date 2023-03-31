/* The following questions test your aptitude for interacting with databases. 
The questions are based off the following public SQL DB: docs.rfam.org/en/latest/database.html
a. How many types of tigers can be found in the taxonomy table of the dataset? 
    What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
b. Find all the columns that can be used to connect the tables in the given database. */

/* a. to find the types of tiger in taxonomy table the sql query will be */
SELECT COUNT(DISTINCT biotype) as num_tigers
FROM taxonomy
WHERE species = 'Panthera tigris sumatrae';


/* to find the ncbi id of tiger smartian */
SELECT ncbi_id
FROM taxonomy
WHERE species = 'Panthera tigris sumatrae';

/* b. to connect all the tables the column used to connect the dataset are 
     "family_acc" column in the "family" table is a foreign key referencing the "rfam_acc" 
     column in the "rna" table, and the "ncbi_id" column in the "taxonomy" table is a foreign key 
     referencing the "ncbi_id" column in the "rna" table. 
     Therefore, these columns can be used to connect the tables in the database
*/