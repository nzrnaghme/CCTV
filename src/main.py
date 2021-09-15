from typing import Any, Dict
import uvicorn
from fastapi import Body, FastAPI
from fastapi import params
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import os


app = FastAPI()

class Intent(BaseModel):
    displayName: str

class Request(BaseModel):
    intent: Intent 
    parameters: Dict[str, Any]


def search(gender,model,color,size):
    
    import pandas as pd
    
    data = pd.read_csv(r"D:\chat data\shoe data.csv", encoding='utf-8')
    
    name_list = data.name
    gender_list = data.gender
    model_list = data.model
    color_list = data.color
    size_list = data.size1
    link_list = data.link1
    
    related_products = []
    related_num = []
    
    for i in range(len(data)):
        
        if gender_list[i] == gender and model_list[i] == model and color_list[i] == color and size_list[i] == size:
            
            related_products.append(name_list[i])
            related_products.append(link_list[i])
            
            related_num.append(name_list[i])
            
        
        tol = len(related_products)
     
        sen = ""
        for i in range(0,tol,2):
            my_shoe_name = related_products[i]
            my_shoe_link = related_products[i+1]
            sen = sen + f" {my_shoe_name}: {my_shoe_link}"             
        
    return(sen,related_num)


def handle_newQuatation(YesNo: str):
    global answer 
    answer = YesNo
    if(answer == "yes"):
         return f"What is your size area?"
    return f"empty empty empty"


def handle_size(number: str):
    global sizeArea 
    sizeArea = number
    return "How many cameras do you want to install? ( 1 to 8 cameras)"


def handle_installCamera(NumberCamera: str):
    global installCamera 
    installCamera = NumberCamera
    return f"how will your cameras be used? (parking/cashier/warehouse/shop store)"


def handle_goalCameras(goalCamera: str):
    global goalCameras 
    goalCameras = goalCamera
    return "chose your model? Boulet/ dome/ 360/ PTZ"

def handle_TypeCameras(typeCamera: str):
    global typeCameras 
    typeCameras = typeCamera
    return "Do you want to store your data? (By default, your data is already stored locally, allowing you to store it for 30 days.)"

def handle_storeData(YesNo: str):
    global storeData 
    storeData = YesNo
    if (storeData == "yes"):
        return "Please Select The options:(HDD on NVR - cloud - local & cloud)"
    else:
        handle_scalableNoSolution(storeData)


def handle_scalableNoSolution(YesNo: str):
    global scalable 
    scalable = YesNo
    return "Would you like a scalable solution? With more cameras in the future?"

def handle_optionStore(optionData: str):
    global storeData 
    storeData = optionData
    return "Would you like a scalable solution storage?(2 T HDD)"

def handle_scalableSolution(YesNo: str):
    global scalable 
    scalable = YesNo
    return "Would you like a scalable solution? With more cameras in the future ?"

def handle_scalableSolutionFuture(YesNo: str):
    global scalable 
    scalable = YesNo
    return "Do you want to view your videos locally in the store? (Watching videos on your smartphone is free and included)"

def handle_videoLocaly(YesNo: str):
    global localy 
    localy = YesNo
    if (localy == "yes"):
        return "which screen do you want for viewing in your store?"
    else:
        handle_videNooLocaly(localy)

def handle_videNooLocaly(YesNo: str):
    global noLocaly 
    noLocaly = YesNo
    return "We need some more information please answer these question, Who is your internet provider?"

def handle_whichScreen(screenSize: str, number: str):
    global noLocaly 
    noLocaly = screenSize
    return "We need some more information please answer these question, Who is your internet provider?"

def handle_internetProvide(screenSize: str):
    global provide 
    provide = screenSize
    return "What is your internet connection?"

def handle_internetConnection(internetConnection: str):
    global connection 
    connection = internetConnection
    return "Do you have a firewall?"

def handle_firewall(YesNoIdonot: str):
    global firewall 
    firewall = YesNoIdonot
    return "Are you the administrator of your network?"

def handle_adminsterOfNetwork(YesNoIdonot: str):
    global adminster 
    adminster = YesNoIdonot
    return "Does the site have ceilings tile?"

def handle_ceilingTile(YesNoIdonot: str):
    global ceiling 
    ceiling = YesNoIdonot
    return "Is the site equipped with a rack or a secure place?"

def handle_EquippedRack(equiped: str):
    global EquippedRack 
    EquippedRack = equiped
    return "Does the site have load-bearing walls?"

def handle_LoadBearing(YesNoIdonot: str):
    global LoadBearing 
    LoadBearing = YesNoIdonot
    return "What is the type of building?( old or modern)"

def handle_typeBuilding(typeBuilding: str):
    global typeBuild 
    typeBuild = typeBuilding
    return "do you need  following training?(3 hour training - In-depth training in the use of the equipment - Become completely autonomous in the use of your system - Maintenance)"

def handle_followTraining(YesNo: str):
    global followTrain 
    followTrain = YesNo
    if( followTrain == "yes"):
        return "add cost 200€, Do you need following maintenance? 10 non-invoiced trips for everything included in the GTC"
    else:
        handle_followTrainingNo(followTrain)

def handle_followMaintance(YesNo: str):
    global followMain 
    followMain = YesNo
    if( followMain == "yes"):
        return "add 15 %  of total quotation  + 200€,  Thanks you."
    else:
        handle_followMaintanceNo(followTrain)

def handle_followTrainingNo(YesNo: str):
    global followTrain 
    followTrain = YesNo
    return "Do you need following maintenance? 10 non-invoiced trips for everything included in the GTC"

def handle_followMaintanceNo(YesNo: str):
    global followTrain 
    followTrain = YesNo
    return "Thanks you."





#     mycase = len(relatedProduct)
#     if mycase > 0:
#         return f" Please enter the desired product number or enter the cancel if you are not interested. ({relatedProduct}) "
#     else:
#         return "sorry Shoes shop has not any shoes according to your request.send cancel to change your order or finish your shopping "


# def handle_Reorder(smodel: str, color: str, size: str ):

#     mysize = int(size)
#     mycolor = color
#     mymodel = smodel

#     relatedProduct = search(mygender,mymodel,mycolor, mysize)

#     mycase = len(relatedProduct)
#     if mycase > 0:
#         return f"OK, I find out your size is {mysize}-{mycolor}-{mymodel}, According to your request,this case ({relatedProduct}) are recommended: Please enter the desired product number or enter the cancel if you are not interested."
#     else:
#         return "sorry Shoes shop has not any shoes according to your request.send cancel to change your order or finish your shopping "


# def handle_address(number: str):
#     global myaddress 
#     myaddress = number
#     return f"OK, it will reach you within the next 3 days. Thanks for your shopping, have good time :D" 



HANDLERS = {
    "GettingNewQuotation": handle_newQuatation,
    "GetSize":handle_size,
    "GettingManyCameras":handle_installCamera,
    "GetModelUseCamera":handle_goalCameras,
    "GetChoseModelType":handle_TypeCameras,
    "GetStoreTypeData":handle_storeData,
    "GetScableNoSolution":handle_scalableNoSolution,
    "GetOptionData":handle_optionStore,
    "GetScalableSolutionStorage":handle_scalableSolution,
    "GetScalableSolutionStorageFuture":handle_scalableSolutionFuture,
    "GetYesVideoLocaly":handle_videoLocaly,
    "GetNoVideoLocalyFuture":handle_videNooLocaly,
    "GetWhichScreen":handle_whichScreen,
    "GetInternetProvide":handle_internetProvide,
    "GetInternetConnection":handle_internetConnection,
    "GetFirewall":handle_firewall,
    "GetAdminesterOfNetwork":handle_adminsterOfNetwork,
    "GetCeilingTile":handle_ceilingTile,
    "GetEquippedRack":handle_EquippedRack,
    "GetLoadBearing":handle_LoadBearing,
    "GetTypeBuilding":handle_typeBuilding,
    "GetYesFollowingTraining":handle_followTraining,
    "GetNoFollowingTraining":handle_followTrainingNo,
    "GetFollowingMaintance":handle_followMaintance,
    "GetNoFollowingMaintance":handle_followMaintanceNo

    # "GettingModel": handle_model,
    # "GettingColor": handle_color,
    # "GettingSize": handle_size,
    # "GettingAddress": handle_address,
    # "GettingReorder": handle_Reorder
}

@app.post("/")
async def home(queryResult: Request = Body(..., embed=True)):
    intent = queryResult.intent.displayName
    print(queryResult.parameters)
    if handler := HANDLERS.get(intent):
        text = handler(**queryResult.parameters)
    else:
        text = "I am not sure to help with that"
    return {"fulfillmentText": text} 