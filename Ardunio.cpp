# include<Ardunio.h>
int adTwoInts(int x, int y)
{
    return x + y;
}

void setup()
{
    Serial.begin()
    int result = addTwoInts(4, 3);
    Serial.println(result)
}

void loop() 
{
  int a = 5;
  int b = 6;
  int result = addTwoInts(a, b);
  Serial.println(result);
  delay(1000); 
}