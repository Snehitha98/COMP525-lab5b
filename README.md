### record_per_row()
```
def record_per_row(self):
    """
    Writes a CSV file with as many records as the size of any of the lists
    A record is a row in the file, with three columns, corresponding to
    a name, salary, and position.
    """
```
* Create 3-field records from the three attributes such that
    * a **record** has elements at the same position in the three lists.
* Format a record as a string with the three elements separated by comma
* Write each record to the **nba.txt** text file

We use the accumulation pattern with **accumulator** `nba_file`
* Iteration is over three sequences simultaneously, the class attributes
    * three loop variables `name`, `salary`, `position` get hold of elements in `self.names`,
    `self.salaries`, `self.positions` which have the same positions
    * we use `zip()` built-in function to allow for parallel processing
    * we assemble string representations of the elements including the commas
    and store in `nba_row` string local variable
    * we write `nba_row` to the file object **accumulator** `nba_file`


### names_by_pos()
```
def names_by_pos(self):
      """
      Create a dictionary keyed by positions and values are lists
      of the names corresponding to each position.
      Returns : dictionary
         keys are positions
         values are list of names that correspond to that position
      """
```
* **file_ref** holds a reference to the file object returned by open
* Use the accumulation pattern
* **accumulator**
    * of type dictionary
    * initialized with {}
    * named `names_by_pos`
    * keys are the positions
    * values are the list of names that correspond to that position
* use a for loop with loop variable named `line` to iterate over `file_ref.readlines()`
    * split the line by comma and store it in variable named `lst`
    * Assign first index of `lst` to `a_name`
    * Assign third index of `lst` to `a_position`
    * replace `\n` of a_position and store it in `a_position`
    * at each iteration check if `a_position` is in `names_by_pos`
       * if it is, add `a_name` of type list, to `names_by_pos` keyed by `a_position` and assign it to `names_by_pos[a_position]`
    * else
       * store the value `a_name` in `names_by_pos` keyed by `a_position`
    * close the opened file `file_ref`
* Returns `names_by_pos` when iteration is over  


### most_played_position()
```
def most_played_position(self):
      """
      call names_by_pos(self), use the dictionary to create a new dictionary
      whose keys are the positions and the values are the lengths of the
      lists of players for each position.
      input : dictionary
         keys are positions
         values are list of names that correspond to that position
      Returns : dictionary
         keys are positions
         values are lengths of the lists of players for each position
      """
```
* Call the function **names_by_pos()**
* Use the accumulation pattern
* **accumulator**
    * of type dictionary
    * initialized with {}
    * named `most_played_position`
    * keys are the positions
    * values are the length of the lists of players for each position
*  use a for loop with loop variable named `key` to iterate over `names_by_pos`
    * define and initialize `len_of_list` of type integer that returns length of list of players `names_by_pos[key]`
    * assign `len_of_list` to `most_played_position` keyed by `key`
* Returns `most_played_position` when iteration is over
