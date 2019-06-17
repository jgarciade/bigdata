# Mongo DB specification

|----------------------------------- DB
                                     |
                                     |

2011  ----  2012  ----  2013  ----  2014  ----  2015  ----  2016  ----  2017
                          |
                          |
                ---------------------------------------
                |   Salary Range --> [int]             |
                |   Region --> String                  |
                |   programming languages --> [String]-|
                |   Satisfaction --> int               |
                |   gender --> String                  |
                |   OS --> [String]                    |
                |   age range --> [int]                |
                |   experience --> [int]               |
                |   company size --> [int]             |
                ----------------------------------------


Age Range: [0, 20] [21, 25] [26, 30] [31, 40] [41, 50] [>50]
Experience: [<20k] [20k, 40k] [40k, 60k] [60k, 80k] [80k, 100k] [100k, 120k] [120k, 140k] [>140k]
company size: [1, 25] [26, 100] [101, 1000] [>1000]
Satisfaction: Subjetive
    2011 --> {enjoy: 5, hurts: 4, not happy: 1, bills: 3}
    2012 --> {love: 5, enjoy: 4, hate: 1, not happy: 2, paycheck: 3, wish a job: None}
    2013 --> {love: 5, enjoy: 4, hate: 1, not happy: 2, paycheck: 3, wish a job: None}
    2015 --> {love: 5, I'm somewhat satisfied with my job: 4, hate: 1, I'm somewhat dissatisfied with my job: 2, I'm neither satisfied nor dissatisfied with my job: 3, Other: None}
    2016 --> {love: 5, I'm somewhat satisfied with my job: 4, hate: 1, I'm somewhat dissatisfied with my job: 2, I'm neither satisfied nor dissatisfied with my job: 3, Other: None, I don't have a job: None}
    2011 --> [nan, 7., 8., 5., 9., 6., 2., 10., 0., 4., 3., 1.]
