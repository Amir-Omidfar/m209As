# Text Entry using 4 square cm input area

## This is UCLA ECE 209As Intro to HCI [Bake Off 1](https://docs.google.com/document/d/19bWmqGldqR1P6aN4QhEY-IQBmL_pcCz_rYCATQQTzks/edit)
 
### Below is the description of how we approach this assignment:

1. The [leap motion sensor](https://www.leapmotion.com) is used for counting the number of fingers exrtended in the user's left/right hand.(We are using numbers 0 through 5)
2. Each 4-5 letters are grouped under the detected numbers 0-5. We use buttons to toggle through and pick the right letter.

   | Number of extended fingers | Alphabets assigned |
   |----------------------------|--------------------|
   |         0                  | a b c d space      |
   |         1                  | e f g h backSapce  |
   |         2                  | i j k l .          |
   |         3                  | m n o p q          |
   |         4                  | r s t u v          |
   |         5                  | w x y z ,          |

3. Our typing technique counts the number of finger shown, it then uses up and down arrow keyboard to confirm the user's selection and simply type. For more info please read our [report](https://github.com/Amir-Omidfar/m209As/blob/master/Bake%20Off%201%20Report%20.pdf)

4. In order to the setup the system, you need to have the leap motion sensor set up. Once the [leap SDK](https://developer.leapmotion.com) is set up. Run the .html file and make sure the leap motion .js file is in the same directory.  

 
5. Here is the link to our [demo]()
