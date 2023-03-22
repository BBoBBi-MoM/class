# data
combat_data = read.csv('./data/combats.csv')
name_data = read.csv('./data/name_data.csv')
pokemon_data = read.csv('./data/pokemon.csv')
vanilla_data = read.csv('./data/vanilla.csv')
normalized_data = read.csv('./data/nomalized.csv')
min_max_data = read.csv('./data/min_max.csv')
kor_pokemon_data = merge(pokemon_data,name_data,by='Name')
kor_pokemon_data= kor_pokemon_data[,c(15,1,2,3,4,5,6,7,8,9,10,11,12,13,14)]
# library
library(shiny)

# function
name_to_index = function(name){
    index = as.numeric(pokemon_data[pokemon_data$name == name,][2])
    return(index)
}
index_to_name = function(index){
    name = as.character(pokemon_data[pokemon_data$index==index,][1])
    return(name)
}

#
abstract_Text = '포켓몬 전투 데이터 5만개를 이용하여 로지스틱 회귀분석을 한 후, 
데이터에 없는 포켓몬끼리의 전투 결과를 예측'
refine_combat_result = function(index,data){
    cat(index_to_name(index),'와 싸운 포켓몬들입니다..',index_to_name(index),'가 졌으면 1 이겼으면 0')
    result_df = combat_data[combat_data$First_pokemon==index|combat_data$Second_pokemon==index,]
    result_df[result_df$First_pokemon==index,][1] = 0
    result_df[result_df$Second_pokemon==index,][2] = 0
    result_df[result_df$Winner==index,][3] = 0
    result_df[result_df$Winner!=0,][3]=1
    result_df$index = result_df$First_pokemon+result_df$Second_pokemon
    result_df=result_df[c(-1,-2)]
    result_df=result_df[,c(2,1)]
    row.names(result_df) = NULL
    output = merge(data,result_df,by='index')
    output = unique(output)
    row.names(output)=NULL
    return(output) 
}
#------------------------------------------------------------------------------------------------------------------------
ui = fluidPage(
  tabsetPanel(
    tabPanel('abstract',textOutput('txt1')),
    tabPanel('preprocessing',
             mainPanel(
               tabsetPanel(
                 tabPanel('원-핫 인코딩',imageOutput('pre',width ='400px'),br(),imageOutput('encoded',width ='400px')),
                 br(),
                 tabPanel("정규화",imageOutput('van',width ='400px'),br(),imageOutput('min_max',width ='400px'),br(),imageOutput('z',width ='400px'))
               )
             )),            
    tabPanel("analizing",
        titlePanel('데이터 분석'),
        mainPanel(dataTableOutput('table_raw'))),
    tabPanel("logistic regression"),
    tabPanel('conclusion',textOutput('txt'))
  ))

server <- function ( input, output, session ){
  van_file = normalizePath(file.path('./images', 'van.PNG'))
  min_max_file = normalizePath(file.path('./images', 'min_max.PNG'))
  z_file = normalizePath(file.path('./images', 'z.PNG'))
  pre_file = normalizePath(file.path('./images', 'pre.PNG'))
  encoded_file = normalizePath(file.path('./images', 'encoded.PNG'))
  output$van<-renderImage(
    {list(src=van_file,
           contentType='image/png', #image/확장자
           alt='This is alternate text')
  },deleteFile = FALSE)

  output$min_max<-renderImage(
    {list(src=min_max_file,
           contentType='image/png', #image/확장자
           alt='This is alternate text')
  },deleteFile = FALSE)

  output$z<-renderImage(
    {list(src=z_file,
           contentType='image/png', #image/확장자
           alt='This is alternate text')
  },deleteFile = FALSE)

  output$pre<-renderImage(
    {list(src=pre_file,
           contentType='image/png', #image/확장자
           alt='This is alternate text')
  },deleteFile = FALSE)

  output$encoded<-renderImage(
    {list(src=encoded_file,
           contentType='image/png', #image/확장자
           alt='This is alternate text')
  },deleteFile = FALSE) 
  output$table_raw <-renderDataTable(vanilla_data,options=list(pageLength=10))
  output$kor_pokemon_data <-renderDataTable(kor_pokemon_data,options=list(pageLength=10))
  output$txt1 = renderText(abstract_Text)
  output$txt = renderText('포켓몬의 세계는 통계따위로 분석할 수 없다. 트레이너의 직감과 포켓몬과의 교감이 중요하다')
  
  
  
} 

shinyApp(ui, server)