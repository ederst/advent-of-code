import java.util.List;
import java.io.BufferedReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Objects;

import java.net.*;
import java.io.*;

class Main {
  
  public static void close(Closeable c) {
    if (c != null) {
        try {
          c.close();
        } catch(Exception e){
          //
        } finally {
          //
        }
    }
  }
  
  public static List<Integer> getResults(int current, List<Integer> previousResults, List<Integer> frequencies) {
      
      List<Integer> results = new ArrayList<>();
      
      int result = current;
      for(Integer frequency : frequencies) {
        result += frequency;

        if (previousResults.contains(result)) {
          results.clear();
          results.add(result);
          return results;
        }

        results.add(result);
      }
      return results;
  }

  public static List<Integer> getFrequencies() {
    //String[] lines = {"7", "7", "-2", "-7", "-4"};

    List<Integer> frequencies = new ArrayList<>();
    BufferedReader reader = null;
    try {
      reader = new BufferedReader(new FileReader(new File("day1.txt")));

      String line;
      while ((line = reader.readLine()) != null) {
        frequencies.add(Integer.parseInt(line));
      }
    } catch (Exception e) {
      //
    } finally {
      close(reader);
    }

    return frequencies;       
  }

  public static void doDayOne() {    
    List<Integer> frequencies = getFrequencies();

    List<Integer> results = getResults(0, Collections.emptyList(), frequencies);

    System.out.println(results.get(results.size() - 1));


      List<Integer> currentResults = null;
      do {
        currentResults = getResults(results.get(results.size() - 1), results, frequencies);

        System.out.println(currentResults.size());

        results.addAll(currentResults);
      } while(currentResults.size() > 1);

      System.out.println(currentResults.get(0));
  }

 
  public static void main(String[] args) {
    doDayOne();
  }
}