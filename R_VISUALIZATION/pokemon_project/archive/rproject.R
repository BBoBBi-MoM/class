library(shiny)

ui <- fluidPage(
    textOutput('txt'),
    fileInput("file", "name file"),
    tableOutput("data"),
    textInput("name", label = "이름", value = ""),
    actionButton("submit", "입력"),
    verbatimTextOutput("result")
)

server <- function ( input, output, session )
{
    output$txt=renderText('포켓몬 전투 분석')
    observeEvent(input$submit, {
        output$result <- renderPrint({
                paste0(input$name, "의 정보..")
                })
            })
    data <- reactive({
    if (is.null(input$file)) {
      return(NULL)
    }
    read.csv(input$file$datapath, header = TRUE)
  })
  
  output$data <- renderTable({
    data()
  })
}



shinyApp( ui = ui, server = server )