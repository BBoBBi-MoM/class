library(shiny)

ui <- fluidPage(
    textOutput('text1'),
    plotOutput('plot1',width='400px'),
    tableOutput('static'),
    dataTableOutput('dynamic')
)


server <- function(input, output, session){
    output$text1 <- renderText('시팔')

    output$plot1 <- renderPlot(
        {
            cars2 <- cars+rnorm(nrow(cars))

            plot(cars2, col='blue', pch=20)
        }
    )

    output$static <- renderTable(head(mtcars))
    output$dynamic <- renderDataTable(mtcars, options = list(pageLenth=5))

}

shinyApp(ui = ui, server = server)