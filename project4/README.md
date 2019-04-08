# **Project 4: B+ Trees**

This project is to be done by yourself.

## **Introduction**

This project was adapted from a B+ tree implementation project originally developed at the University of California Berkeley. The goal of this project is to give you a deeper understanding of how B+ trees work. The best way to accomplish this is by building one yourself. Do not fear, you will not be writing this from scratch!  Methods you will need to implement will have comments telling you what to do.  More on this later.

## **Environment**

We will not be using the virtual machine environment that we've been using for the other projects thus far this semester, since this is a pure Java project.  We highly recommend you install/use an IDE like Eclipse for this project.  We will be using Maven to run the tests.  If you can import the code as a Maven project in your IDE and run your unit tests successfully, you do not need to install Maven on your local computer. Most IDEs should provide this functionality by default. For example, in Eclipse, you can do this: File > import > maven > existing maven project.

Or if you don't want to use IDE, you can also do the same thing through command lines:

```bash
    # use MacBook
    brew install maven
    cd project4
    # build code without testing
    mvn package -Pdist -DskipTests
    # build code and run unit tests
    mvn package -Pdist
```

## **The Project Files**

To begin, pull the Project 4 folder from our repository as always.  Here is a brief overview.  You should primarily be focused on the contents of the index directory:

### index
The 'index' directory contains all the files that you will need to edit, specifically, LeafNode.java, InnerNode.java, and BPlusTree.java.  

* **BPlusNode.java**: An abstract class for LeafNode and InnerNode. This contains very important information on how to implement methods in those two classes.  Make sure you follow what is written here!

* **LeafNode.java**: Leaf nodes class.  You will need to implement some methods in this.

* **InnerNode.java**: Inner nodes class.  You will need to implement some methods in this.

* **BPlusTree.java**: B+ Tree class.  This is the structure that will hold LeafNodes and InnerNodes.  You will need to implement some methods in this.

### common
The 'common' directory contains miscellaneous but handy bits of code.

### databox
The 'databox' directory contains classes which represent the values stored in a database as well as their types. Specifically, the DataBox class represents values and the Type class represents types. Here's an example:

```java
DataBox x = new IntDataBox(42); // The integer value '42'.
Type t = Type.intType();        // The type 'int'.
Type xsType = x.type();         // Get x's type: Type.intType()
int y = x.getInt();             // Get x's value: 42
String s = x.getString();       // An exception is thrown.
```

### io
The `io` directory contains code that allows you to allocate, read, and write
pages to and from a file. All modifications to the pages of the file are
persisted to the file. The two main classes of this directory are
`PageAllocator` which can be used to allocate pages in a file, and `Page` which
represents pages in the file.  Below are some examples of how this works so you can get an idea of it:

Here is an example of how to persist data into a file using a `PageAllocator`:

```java
// Create a page allocator which stores data in the file "foo.data". Setting
// wipe to true clears out any data that may have previously been in the file.
bool wipe = true;
PageAllocator allocator = new PageAllocator("foo.data", wipe);

// Allocate a page in the file. All pages are assigned a unique page number
// which can be used to fetch the page.
int pageNum = allocator.allocPage(); // The page number of the allocated page.
Page page = allocator.fetchPage(pageNum); // The page we just allocated.
System.out.println(pageNum); // 0. Page numbers are assigned 0, 1, 2, ...

// Write data into the page. All data written to the page is persisted in the
// file automatically.
Buffer buf = page.getBuffer(transaction);
buf.putInt(42);
buf.putInt(9001);
```

Here is an example of how to read data that's been persisted to a file:

```java
// Create a page allocator which stores data in the file "foo.data". Setting
// wipe to false means that this page allocator can read any data that was
// previously stored in "foo.data".
bool wipe = false;
PageAllocator allocator = new PageAllocator("foo.data", wipe);

// Fetch the page we previously allocated.
Page page = allocator.fetchPage(0);

// Read the data we previously wrote.
Buffer buf = page.getBuffer(transaction);
int x = buf.getInt(); // 42
int y = buf.getInt(); // 9001
```

### table
The 'table' directory used to contain other table related things but you only need the 'RecordId' class which uniquely identifies a record on a page by its page number and entry number:

```java
// The jth record on the ith page.
RecordId rid = new RecordId(i, (short) j);
```

There are a few other files that are used to make the tests work that you are welcome to look at if you need to.

## **Your Tasks**
1. Familiarize yourself with the code in the 'index' directory.  Here is a repeat of a few critical points:
    - Our implementation of B+ trees does not support duplicate keys. You need to throw an exception whenever a duplicate key is inserted.
    - Our implementation of B+ trees assumes that inner nodes and leaf nodes can be serialized on a single page. You do not have to support nodes that span multiple pages.
    - Our implementation of delete does not rebalance the tree. Thus, the rule that all non-root leaf nodes in a B+ tree of order `d` contain between `d` and `2d` entries will not hold for this project. Note that actual B+ trees **do rebalance** after deletion, but we will **not** be implementing rebalancing trees in this project for the sake of simplicity.  This means you also do not need to account for cases where inner nodes may be deleted.  
2. Implement the `LeafNode::fromBytes` function that reads a `LeafNode` from a page. For information on how a leaf node is serialized, see `LeafNode::toBytes`. For an example on how to read a node from disk, see `InnerNode::fromBytes`.
3. Implement the `get`, `getLeftmostLeaf`, `put`, `remove`, and `bulkLoad` methods of `InnerNode` and `LeafNode`. For information on what these methods do, refer to the comments in `BPlusNode`. Don't forget to call `sync` when implementing `put`, `remove`, and `bulkLoad`.
4. Implement the `get`, `scanAll`, `scanGreaterEqual`, `put`, `remove`, and `bulkLoad` methods of `BPlusTree`. In order to implement `scanAll` and `scanGreaterEqual`, you will have to complete the `BPlusTreeIterator` class (`hasNext` and `next`).  The `BPlusTreeIterator` class is an inner class located at the end of the BPlusTree.java file.  To get an idea of what the iterator should do, take a look at the comments for `scanAll` or `scanGreaterEqual`. 

## **Things to Note**

1. This project uses a variable, d, to describe the "order" of a B+ Tree. 2d is defined as the number of **values** in a node (this is true both for leaf nodes and internal nodes). In contrast, the textbook we are using for our class uses a variable, n, to describe the size of nodes in the B+ tree. n is defined as the number of **pointers** in a node. Every node in a B+ tree --- both leaf nodes and internal nodes --- have one more pointer than value. So the n from your textbook is always 2d + 1. Therefore, when the textbook writes, "Each leaf can hold up to n − 1 values. We allow leaf nodes to contain as few as (n−1)/2 (ceiling) values.", this translates to "Every leaf in a B+ tree of order d stores between d and 2d (key, record id) pairs and a pointer to its right sibling." for this project (since 2d = n-1). Thus, there is no difference between the size constraints of nodes between this project and your textbook. You should be aware of how d is defined and how n is defined, and how n = 2d+1, for quizzes and exams.

![node explanation](nodes.png)

2. The order (d) of a B+ Tree is given upon the tree's creation within its metadata field which is passed onto its inner nodes and leaf nodes.
3. Although there are a lot of files included in this project, you do not need to have a robust understanding of them except for the methods in the index directory that you need to implement.
4. You may not modify the signature of any methods or classes that we provide to you (except `BPlusTreeIterator`), but you're free to add helper methods in LeafNode.java, InnerNode.java, and BPlusTree.java.

## **Testing**
All of the tests for this project are in the edu.berkeley.cs186.database.index package in the src/test/java folder.  These will be the only tests we use to run your project.  In Eclipse, you can run the tests by going to your Package Explorer > right-click on the edu.berkeley.cs186.database.index package > Run As > JUnit Test.  You can also right-click on the individual tests to run them separately.

## **Submitting**
Just submit your LeafNode.java, InnerNode.java, and BPlusTree.java to ELMS.
