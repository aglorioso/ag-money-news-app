The file called pac_contrib_aug_15_17_geo.xlsx is the final file I'm working on. For this doc, I copied the all_pacs_contrib tab from the file caldwell_pacs.xlsx, then I saved it as caldwell_all_pacs_contrib_aug_15_17.xlsx and uploaded into datascience studio and geocoded the addresses. I did the same for expenditures

I then went through pac_contrib_aug_15_17_geo.xlsx and cleaned up the names of contributors. When I cleaned them based on their addresses, I made a note, EXCEPT FOR THE CITRUS NAMES I CHANGED TO US SUGAR -- I NEED TO NOTE THOSE.

I'm working on a story about who is supporting the three major GOP candidates in the agricutural race. 

For the shorter story, I also calculated what percentage of Southwest Florida voted in the Presidental/senate primary. I compared to the population size those counties take up in Florida. 

I couldn't get some of the fields to geocode for pac_contrib_aug_15_17_geo.xlsx, so I uploaded them into a website called geocodio (https://dash.geocod.io/import) and that worked. The separte file for that upload was called contrib_not_geocoded and the file it gave me is called contrib_not_geocoded_geocodio...csv. I copied these values back into pac_contrib_aug_15_17_geo.xlsx.

Expenditures is still in datascience studio and isn't geocoding and I don't know why.

Those files:

1. fla_counties_by_population
2. Republican primary presidential, downloaded: 03152016Election.xlsx
3. Florida Senate primary, after augmented in Tableau: fla_senate_primary_2016.xlsx (this also contains the relevant tab from swfl_senate_primary_2016.xlsx)
4. Florida presidential primary after augmented in Tableau: total_fla_repub_presidential_primary.xlsx
5. Florida SWFL Senate primary after augmented in Tableu: swfl_senate_primary_2016.xlsx
6. Senate primary downloaded: 083022016Election.xlsx