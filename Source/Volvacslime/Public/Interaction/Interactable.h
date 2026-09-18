// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "Interactable.generated.h"

UINTERFACE(MinimalAPI, Blueprintable)
class UInteractable : public UInterface
{
	GENERATED_BODY()
};

/**
 * An interface class for objects that can be interacted
 */
class VOLVACSLIME_API IInteractable
{
	GENERATED_BODY()

public:

	/* 
	* Called when the player interact with an object
	* @param Interactor The actor that is interacting with this object
	*/
	UFUNCTION(BlueprintNativeEvent, Category = "Interaction")
	void OnInteract(AActor* Interactor);
	virtual void OnInteract_Implementation(AActor* Interactor) {};

	/**
	* Called when the player swallows an object
	* @param Interactor The actor that is swallowing this object
	*/
	UFUNCTION(BlueprintNativeEvent, Category = "Interaction")
	void OnSwallow(AActor* Interactor);
	virtual void OnSwallow_Implementation(AActor* Interactor) {};

	/**
	* Called when the player spits out an object
	* @param Interactor The actor that is spitting out this object
	* @param LaunchImpulse The impulse applied to the object when it is being spit out
	*/
	UFUNCTION(BlueprintNativeEvent, Category = "Interaction")
	void OnSpitOut(AActor* Interactor, float LaunchImpulse);
	virtual void OnSpitOut_Implementation(AActor* Interactor, float LaunchImpulse) {};
};
