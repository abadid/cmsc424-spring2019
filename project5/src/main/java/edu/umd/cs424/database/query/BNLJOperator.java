package edu.umd.cs424.database.query;

import java.util.*;

import edu.umd.cs424.database.Database;
import edu.umd.cs424.database.DatabaseException;
import edu.umd.cs424.database.common.BacktrackingIterator;
import edu.umd.cs424.database.databox.DataBox;
import edu.umd.cs424.database.io.Page;
import edu.umd.cs424.database.table.Record;

public class BNLJOperator extends JoinOperator {
    public BNLJOperator(QueryOperator leftSource,
                        QueryOperator rightSource,
                        String leftColumnName,
                        String rightColumnName,
                        Database.Transaction transaction) throws QueryPlanException, DatabaseException {
        super(leftSource,
              rightSource,
              leftColumnName,
              rightColumnName,
              transaction,
              JoinType.BNLJ);

        this.stats = this.estimateStats();
        this.cost = this.estimateIOCost();
    }

    public Iterator<Record> iterator() throws QueryPlanException, DatabaseException {
        return new BNLJIterator();
    }

    public int estimateIOCost() throws QueryPlanException {
        //does nothing
        return 0;
    }

    /**
     * BNLJ: Block Nested Loop Join
     *  See Section 12.5.2 of the textbook.
     *
     * An implementation of Iterator that provides an iterator interface for this operator.
     *
     * Before proceeding, you should read and understand SNLJOperator.java
     *    You can find it in the same directory as this file.
     *
     * Word of advice: try to decompose the problem into distinguishable sub-problems.
     *    This means you'll probably want to add more methods than those given (Once again,
     *    SNLJOperator.java might prove to be a useful reference).
     */
    private class BNLJIterator extends JoinIterator {
        /**
         * Some member variables are provided for guidance, but there are many possible solutions.
         * You should implement the solution that's best for you, using any member variables you need.
         * You're free to use these member variables, but you're not obligated to.
         */

        // private Iterator<Page> leftIterator = null;
        // private Iterator<Page> rightIterator = null;
        // private BacktrackingIterator<Record> leftRecordIterator = null;
        // private BacktrackingIterator<Record> rightRecordIterator = null;
        // private Record leftRecord = null;
        // private Record rightRecord = null;
        // private Record nextRecord = null;

        public BNLJIterator() throws QueryPlanException, DatabaseException {
            super();
            throw new UnsupportedOperationException("TODO(Project 5): implement");
        }

        private void fetchNextRecord() throws DatabaseException {
            throw new UnsupportedOperationException("TODO(Project 5): implement");
        }

        /**
         * Checks if there are more record(s) to yield
         *
         * @return true if this iterator has another record to yield, otherwise false
         */
        public boolean hasNext() {
            throw new UnsupportedOperationException("TODO(Project 5): implement");
        }

        /**
         * Yields the next record of this iterator.
         *
         * @return the next Record
         * @throws NoSuchElementException if there are no more Records to yield
         */
        public Record next() {
            throw new UnsupportedOperationException("TODO(Project 5): implement");
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
}

