Hey this is our repo for SnapSecure! Let's use https://github.com/AsamK/signal-cli

This codebase contains plenty of bugs, and glaring security holes. But hey, that's what this class is about, right?

Some of the most glaring errors are marked `XXX`, and feel free to open issues and pull requests with your questions, fixes, and discussions.


#Dependency Instructions

##Signal-Cli install instructions:
###1. Download File:
    1. Download ZIP from [HERE!](https://github.com/AsamK/signal-cli)
    2. Unzip file
    3. Move signal-cli to desktop
    4. Open Terminal/Command line (application)
    5.

        $ cd Desktop/signal-cli

####OR

###Git:
  Checkout the source somewhere on your filesystem with

      $ git clone https://github.com/AsamK/signal-cli.git
      $ cd signal-cli

###2. Execute Gradle:

      $ ./gradlew build

  - May instruct you to [download java](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)

###3. Create shell wrapper in build/install/signal-cli/bin:

      $ ./gradlew installDist

###4. Create tar file in build/distributions:

      $ ./gradlew distTar

#####Maybe needed

###5. Possible fix if you receive signal-cli command not found:
    * navigate to the bin folder

      $ cd signal-cli/build/install/signal-cli/bin
      $ Export PATH for signal-Cli
      $ export PATH=$PATH:/$(pwd)
