What LIBSVM did to the AmazonCat-13K dataset:
  - Cross-check raw data from The Extreme Classification Repository and AttentionXML, and make sure no instances are missing.
  - Clean raw text from The Extreme Classification Repository, put labels in the front, use \t to separate, and put titles and contents behind.
  - Convert to if-idf features with different configurations.
So I do exactly the same thing to the Amazon-3M dataset:
  - First run compare_files.py to check if instances aren't missing. I remove all spaces and \t from each instance and check if the two strings are the same.
  - Second run preprocess_Amazon-3M.py. It's modified from Amazon-670K_code. I removed the scraper part, it's broken anyway.
  - Lastly run tfidf_Amazon-3M.py to vectorize with the configuration as we did for AmazonCat-13K and Amazon-670K.
What I should do next:
  - I should use the preprocessed data to actually train a model so that I can check if it really boosts performance. I did try for a bit, but I lack of experiences to deal with such a huge dataset,
  so I faced some difficulty. Then I decided to stop right here and make a report before I move forward.
