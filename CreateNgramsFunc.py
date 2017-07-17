import ling


def NgramStat(Infile, Outfile_freq, Outfile_rare, nmin, nmax, rare_max):
     tfile = open(Outfile_freq, 'w', encoding="utf-8")  # encoding="ISO-8859-1")
     if rare_max > 0:
          ufile = open(Outfile_rare, 'w', encoding="utf-8")  
     with open(Infile, 'r', encoding="utf-8") as corpus:
         out = corpus.read()
         output = ling.WordNgramStat(out, nmin, nmax)
     for w in sorted(output, key=output.get, reverse = True):
          if output[w] <= rare_max:
               if Outfile_rare == "": break
               line = '{:>8}'.format(output[w]) + '\t' + w    # rare occurrences
               ufile.write(line + '\n')
          else:
               line = '{:>8}'.format(output[w]) + '\t' + w
               tfile.write(line + '\n')
     tfile.close()
     if rare_max < 0:
          ufile.close()


#NgramStat("..\\sources\\corpus_derma_sorted_cleaned_shuffled_90.txt", "..\\stat\\corpus_derma_sorted_cleaned_shuffled_90_token_stat.txt", "", 1, 1, 0)
#NgramStat("..\\sources\\corpus_cardio_sorted_cleaned_shuffled_90.txt", "..\\stat\\corpus_cardio_sorted_cleaned_shuffled_90_token_stat.txt", "", 1, 1, 0)
#NgramStat("..\\sources\\corpus_derma_sorted_cleaned_shuffled_90.txt", "..\\stat\\corpus_derma_sorted_cleaned_shuffled_90_bigram_stat.txt", "", 2, 2, 0)
#NgramStat("..\\sources\\corpus_cardio_sorted_cleaned_shuffled_90.txt", "..\\stat\\corpus_cardio_sorted_cleaned_shuffled_90_bigram_stat.txt", "", 2, 2, 0)


#NgramStat("S:\Resources\MEDLINE_Cancer\MEDLINE_CANCER_TIAB.txt", "S:\Resources\MEDLINE_Cancer\MEDLINE_CANCER_TIAB_1_10_tokenStat.txt", "", 2, 8, 2)




#NgramStat("Z:\\DocumentCleansing\\CardioCorpusSplit\\script\\trainingCleaned.txt", "..\\stat\\corpus_cardio_training_cleaned_1_to_7gram_stat.txt", "", 1, 7, 0)


#f = open("C:\\Users\\schulz\\Nextcloud\\Terminology\\Corpora\\GR_ABSTRACTS.txt", 'w)


NgramStat("C:\\Users\\schulz\\Nextcloud\\Terminology\\Corpora\\NONGR_ABSTRACTS.txt", "..\\stat\\NONGR_ABSTRACTS_stat.txt", "", 1, 7, 2)


#NgramStat("C:\\Users\\schulz\\Dropbox\\Aktuell\\review\\AO\\ao-paper-461.txt", "..\\stat\\aopaper_stat.txt", "..\\stat\\aopaper_single_stat.txt", 1, 1, 1)