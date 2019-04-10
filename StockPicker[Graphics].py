from graphics import *
def main():

#starting window

    #open window

    win = GraphWin("Stock Picker Instructions", 500, 500)
    win.setCoords(0, 0, 5.0, 5.0)
    win.setBackground(color_rgb(204,238,255))

    #make title of project

    cover = Text(Point(2.5,3), "Stock Picker 1.0")
    cover.setSize(36)
    cover.setFill('green')
    cover.setStyle('bold')
    cover.draw(win)

    #make author text

    author = Text(Point(2.5,2.5), "Coded By: Bryce Gressani")
    author.setSize(16)
    author.setFill('green')
    author.setStyle('bold')
    author.draw(win)

    cla = Text(Point(2.5,2), "CSC 2280 Project")
    cla.setSize(16)
    cla.setFill('green')
    cla.setStyle('bold')
    cla.draw(win)

    #make button

    button = Text(Point(1, .75), "Click Here")
    button.setStyle('bold')
    button.draw(win)
    Rectangle(Point(.5, .5), Point(1.5, 1)).draw(win)

    #go to next window

    win.getMouse()
    win.close()

#Teach users what the indicators used mean

    #open window

    win=GraphWin("Stock Picker Instructions",500,500)
    win.setCoords(0,0,5.0,5.0)
    win.setBackground(color_rgb(204,238,255))

    #make header

    topcenter = (Point(2.5, 4.8))
    firstheader= Text(topcenter, "Lets make some MONEY!")
    firstheader.setSize(16)
    firstheader.setFill('green')
    firstheader.setStyle('bold')
    firstheader.draw(win)
    Line(Point(0,4.7),Point(5,4.7)).draw(win)

    entry1pg1 = Text(Point(2.25,4.5), "Before we start, lets go over a few basics about the indicators used in the picker.")
    entry1pg1.setStyle('bold')
    entry1pg1.setFill('red')
    entry1pg1.setSize(12)
    entry1pg1.draw(win)

    #why use indicators

    #question 1

    entry2pg1 = Text(Point(1.2,4.3), " Q1) Why do we use these indicators?")
    entry2pg1.setSize(12)
    entry2pg1.setStyle('bold')
    entry2pg1.draw(win)

    #answer 1

    entry3pg1 = Text(Point(2.5,4), "Answer) Indicators are used becasue they help determine when a stock is at a good point\n to buy or sell it")
    entry3pg1.setSize(12)
    entry3pg1.draw(win)

    #what indicators are being used

    #question 2

    entry4pg1 = Text(Point(1.42, 3.7), "Q2) What indicators is the picker going to use?")
    entry4pg1.setSize(12)
    entry4pg1.setStyle('bold')
    entry4pg1.draw(win)

    #answer 2

    entry5pg1 = Text(Point(2.3, 3.35), "Answer) The indicators we will use consist of the EMA line, SMA line, MACD, RSI,\n Daily Volume, Price of the Stock, Profit Margin and Margin for Loss ")
    entry5pg1.setSize(12)
    entry5pg1.draw(win)

    #What settings should you use for these settings

    #question 3

    entry6pg1 = Text(Point(1.47, 3), "Q3) What settings should the indicators be set to?")
    entry6pg1.setSize(12)
    entry6pg1.setStyle('bold')
    entry6pg1.draw(win)

    #answer 3

    entry7pg1 = Text(Point(1.8, 2.7), "Answer) Everyone has preferences on what settings they like. \nIn the future I could say what settings I personally like")
    entry7pg1.setSize(12)
    entry7pg1.draw(win)

    #make button

    button= Text(Point(1,.75),"Click Here")
    button.setStyle('bold')
    button.draw(win)
    Rectangle(Point(.5,.5),Point(1.5,1)).draw(win)

    #go to next window

    win.getMouse()
    win.close()

#........................................................................................

#what does each indicator mean

    #open window

    win=GraphWin("Stock Picker Instructions",500,500)
    win.setCoords(0,0,5.0,5.0)
    win.setBackground(color_rgb(204,238,255))

    #make header

    header = Text(topcenter, "What Does Each Indicator Mean/ Why Do We Care?")
    header.setSize(16)
    header.setFill('green')
    header.setStyle('bold')
    header.draw(win)

    Line(Point(0,4.7),Point(5,4.7)).draw(win)

    #explain ema

    defofema = Text(Point(2.1,4.3), "1) The EMA line is typically a good indicator to determine if the stock is moving \n\tgenerally in a upward or downward direction. It gives more importance to newer data. ")
    defofema.setSize(12)
    defofema.draw(win)

    #explain sma

    defofsma = Text(Point(2.05,3.9), "\n2) The SMA like the EMA tells if the stock is moving upward or downward but \rdoes not give newer data more importance.")
    defofsma.setSize(12)
    defofsma.draw(win)

    #explain profit margin

    defofmargin = Text(Point(2.05,3.5), "\n3) We want to know the margin of profit possible because if the risk to reward \rratio is not at least 3x than my standards say it is not worth buying.")
    defofmargin.setSize(12)
    defofmargin.draw(win)

    #explain cost of stock

    defofcost = Text(Point(1.95,3.05), "\n4) We care about the cost of a stock because if it is trading at too cheap a \rprice than it will inherently be more risky to buy.")
    defofcost.setSize(12)
    defofcost.draw(win)

    #explain daily volume

    defofvolume = Text(Point(2.02, 2.65), "\n5) Daily Volume is important because if a stock has too low of volume then it \rwill likely be more volatile and harder to predict.")
    defofvolume.setSize(12)
    defofvolume.draw(win)

    #explain rsi indicator

    defofrsi = Text(Point(2.24,2.25), "\n6) The RSI is used to tell whether a stock is more overbought or oversold. The higher \r\tthe RSI the more overbought the stock is, conversely the lower the RSI the more oversold.")
    defofrsi.setSize(12)
    defofrsi.draw(win)

    #explain MACD

    defofmacd = Text(Point(2.25,1.7), "\n7) The MACD is also used to show whether a stock is being bought more or sold more.\r Ideally you would buy when the curve is pointing or starting to point up \r(meaning it is starting to be bought more).")
    defofmacd.setSize(12)
    defofmacd.draw(win)

    Line(Point(0,1.2), Point(5,1.2)).draw(win)

    #make button

    button = Text(Point(1, .75), "Click Here")
    button.setStyle('bold')
    button.draw(win)
    Rectangle(Point(.5, .5), Point(1.5, 1)).draw(win)

    #next window

    win.getMouse()
    win.close()


#........................................................................................

#Stock Picker Instruction window

    #open window

    win=GraphWin("Stock Picker Instructions",500,500)
    win.setCoords(0,0,5.0,5.0)
    win.setBackground(color_rgb(204,238,255))

#Instructions for using stock picker.................

    #make header

    header= Text(topcenter, "Instructions for Using the Stock Picker")
    header.setSize(16)
    header.draw(win)
    Line(Point(0,4.7),Point(5,4.7)).draw(win)
    rules= Text(Point(2.5,4.5), "Rules")
    rules.setStyle('bold')
    rules.setFill('red')
    rules.draw(win)
    
    #text for instructions

    #rule 1

    rule1= Text(Point(1.48, 4.25), "1) If the answer is 'yes' or 'no' use '1' for 'yes' and '0' for no")
    rule1.setFill('blue')
    rule1.draw(win)

    #rule2

    rule2= Text(Point(2.17, 4), "2) If the question requires a numeric entry just enter the number, no words or symbols")
    rule2.setFill('blue')
    rule2.draw(win)

    #rule3

    rule3= Text(Point(1.76, 3.75), "3) Don't click on the screen unless it is a text entry box or instructed to")
    rule3.setFill('blue')
    rule3.draw(win)

    #rule4

    rule4= Text(Point(2.02, 3.5), "4) Be sure to answer every question, If you don't know the answer then estimate")
    rule4.setFill('blue')
    rule4.draw(win)

    button.draw(win)
    Rectangle(Point(.5,.5),Point(1.5,1)).draw(win)

    #go to next window

    win.getMouse()
    win.close()
    
#Actual Stock Picker window

    #open window

    win=GraphWin("Stock Picker", 500,500)
    win.setCoords(0,0,5.0,5.0)
    win.setBackground(color_rgb(204,238,255))
    
#draw box where inputs are entered

    pickerheader= Text(topcenter, "Answer Questions Below to Make $$$")
    pickerheader.setStyle('bold')
    pickerheader.setFill('green')
    pickerheader.draw(win)

#........................................................................................

#make the text for parameter  questions

    #make text entry for ema

    ematext= Text(Point(.91,4.5), "Is the stock trading above the EMA")
    ematext.setFill('blue')
    ematext.draw(win)

    #make text entry for sma

    smatext= Text(Point(1,4), "Is the SMA Acting as a close resistance")
    smatext.setFill('blue')
    smatext.draw(win)

    #make text entry for profit margin

    profittext= Text(Point(1,3.5),"What is the % Margin of Profit Available")
    profittext.setFill('blue')
    profittext.draw(win)

    #make text for margin loss

    losstext= Text(Point(.97,3), "What is the % Margin of Loss Possible")
    losstext.setFill('blue')
    losstext.draw(win)

    #make text entry for stock cost

    costtext= Text(Point(.92,2.5), "What is the current cost of the stock")
    costtext.setFill('blue')
    costtext.draw(win)

    #make text entry for daily volume

    volumetext= Text(Point(.95,2),"What is the daily volume of the stock")
    volumetext.setFill('blue')
    volumetext.draw(win)

    #make text entry for rsi number

    rsitext= Text(Point(.59,1.5), "What is the RSI Value")
    rsitext.setFill("blue")
    rsitext.draw(win)

    #Create lines to divide indicators

    Line(Point(0,4.4),Point(4,4.4)).draw(win)
    Line(Point(0,3.9),Point(4,3.9)).draw(win)
    Line(Point(0,3.4),Point(4,3.4)).draw(win)
    Line(Point(0,2.9),Point(4,2.9)).draw(win)
    Line(Point(0,2.4),Point(4,2.4)).draw(win)
    Line(Point(0,1.9),Point(4,1.9)).draw(win)
    Line(Point(0,1.4),Point(4,1.4)).draw(win)
    
#........................................................................................

#Create the entry boxs

    #create ema entry box

    inputema= Entry(Point(4,4.5),15)
    inputema.setText("'1' for yes or '0' for no")
    inputema.setFill('white')
    inputema.setTextColor('red')
    inputema.draw(win)
   
    #sma entry box

    inputsma=Entry(Point(4,4),15)
    inputsma.setText("'1' for yes or '0' for no")
    inputsma.setFill('white')
    inputsma.setTextColor('red')
    inputsma.draw(win)

    #profit margin box

    inputprofitmargin= Entry(Point(4,3.5),15)
    inputprofitmargin.setText("No '%' symbol")
    inputprofitmargin.setFill('white')
    inputprofitmargin.setTextColor('red')
    inputprofitmargin.draw(win)

    #margin loss possible box

    inputmarginloss= Entry(Point(4,3),15)
    inputmarginloss.setText("No '%' symbol")
    inputmarginloss.setFill('white')
    inputmarginloss.setTextColor('red')
    inputmarginloss.draw(win)

    #cost of stock box

    inputstockcost= Entry(Point(4,2.5),15)
    inputstockcost.setText("No '$' in answer")
    inputstockcost.setFill('white')
    inputstockcost.setTextColor('red')
    inputstockcost.draw(win)

    #daily volume box

    inputvolume= Entry(Point(4,2),15)
    inputvolume.setText("Daily Volume")
    inputvolume.setFill('white')
    inputvolume.setTextColor('red')
    inputvolume.draw(win)

    #rsi value box

    inputrsi= Entry(Point(4,1.5),15)
    inputrsi.setText("RSI Value")
    inputrsi.setFill('white')
    inputrsi.setTextColor('red')
    inputrsi.draw(win)

    #make button

    button= Text(Point(1,.75),"Get Advice")
    button.draw(win)
    Rectangle(Point(.5,.5),Point(1.5,1)).draw(win)


    #click to save inputs

    win.getMouse()

    #variable to use for respose

    emaanswer=int(inputema.getText())
    smaanswer=int(inputsma.getText())
    profitmargin=int(inputprofitmargin.getText())
    marginloss=int(inputmarginloss.getText())
    riskreward=profitmargin/marginloss
    stockcost=float(inputstockcost.getText())
    volume=int(inputvolume.getText())
    rsi=float(inputrsi.getText())
    
# Advice for user ....................................................................................

#instant buys

    if(emaanswer==1 and smaanswer==0 and riskreward>=3 and stockcost>5 and volume>=100000 and rsi<=40):
        Text(Point(4,.75),"Buy, indicators say this is a good buy!").draw(win)

#instant no buys

    #price too low

    elif(stockcost<=5):
        Text(Point(3.5,.75), "Dont buy at all, indicators are not favorable").draw(win)

    #risk not worth it

    elif(riskreward<3):
        Text(Point(3.5,.75),"Dont buy at all, indicators are not favorable").draw(win)

    #volume not high enough

    elif(volume<20000):
        Text(Point(3.5,.75), "Dont buy at all, indicators are not favorable").draw(win)
        Text(Point(3.5, .60), "Low volume will typically make a stock more volatile").draw(win)

    #rsi too high

    elif(rsi>=60):
        Text(Point(3.5,.75),"Dont buy at all, indicators are not favorable").draw(win)
        Text(Point(3.5, .60), "High RSI makes a decrease in price likely").draw(win)

#Maybe buys

    #ema good, sma bad

    elif(emaanswer==1 and smaanswer==1 and volume>20000 and riskreward>=3 and rsi<=40):
        Text(Point(3.5,.75),"You can buy, but watch for resistance").draw(win)
        Text(Point(3.5,.6), "An SMA acting as a resistance is concerning")

   #ema could be resistance

    elif(emaanswer==0):
        Text(Point(3.5,.75),"Any time a stock is below the EMA line it is risky to buy").draw(win)
        Text(Point(3.5, .6), "An EMA acting as a resistance is concerning").draw(win)

    #combination of inputs is not in code

    else:
        Text(Point(3.5,.75),"Not yet an answer for this combination of inputs").draw(win)
        Text(Point(3.5, .60), "Enter different values or try a new stock").draw(win)

    #go to next window

    win.getMouse()
    win.close()

#Closing window.................................................................................

    #open window

    win=GraphWin("Stock Picker", 500,500)
    win.setCoords(0,0,5.0,5.0)
    win.setBackground(color_rgb(204,238,255))

    #Create Text for closing window

    thanks = Text(Point(2.5, 3.5), "THANK YOU FOR USING THE STOCK PICKER!")
    thanks.setSize(20)
    thanks.setStyle('bold')
    thanks.draw(win)

    #sorry if code doesnt have an answer

    sorry = Text(Point(2.5, 2.5), "Sorry if your criteria didn't have an answer!")
    sorry.setSize(16)
    sorry.setStyle('bold')
    sorry.draw(win)

    update = Text(Point(2.5, 2), "Updates coming that will add more answers to different criteria")
    update.setSize(16)
    update.setStyle('bold')
    update.draw(win)

    #close program

    win.getMouse()
    win.close()


main()


