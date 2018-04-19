Hey this is our repo for SnapSecure! Let's use https://github.com/AsamK/signal-cli

This codebase contains plenty of bugs, and glaring security holes. But hey, that's what this class is about, right?

Some of the most glaring errors are marked `XXX`, and feel free to open issues and pull requests with your questions, fixes, and discussions.



Signal-Cli install instructions:
1-Download File:
  Download ZIP from [HERE!](https://github.com/AsamK/signal-cli)
  Unzip file
  move signal-cli to desktop

OR

  Git:
  Checkout the source somewhere on your filesystem with
    $ git clone https://github.com/AsamK/signal-cli.git
    $ cd signal-cli
2-Execute Gradle:
    ./gradlew build
      -may ask for you to download java
[link](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)

3-Create shell wrapper in build/install/signal-cli/bin:
  ./gradlew installDist

4-Create tar file in build/distributions:
  ./gradlew distTar

Maybe needed
5-Possible fix if you receive signal-cli command not found:
    navigate to the bin folder
      $ cd signal-cli/build/install/signal-cli/bin

      Export PATH for signal-Cli
      $ export PATH=$PATH:/$(pwd)
