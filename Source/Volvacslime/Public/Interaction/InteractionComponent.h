// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "InteractionComponent.generated.h"

class USphereComponent;

/**
 * A component that allows the player to interact with objects in the world
 */
UCLASS(ClassGroup = ("Interaction"), meta = (BlueprintSpawnableComponent))
class VOLVACSLIME_API UInteractionComponent : public UActorComponent
{
	GENERATED_BODY()

public:	
	UInteractionComponent();

	/** The collision channel used to detect interactable objects */
	UPROPERTY(EditAnywhere, Category = "Interaction|Physics")
	ECollisionChannel CollisionChannel = ECC_Visibility;

	/** The force applied to the object when it is being pulled towards the player */
	UPROPERTY(EditAnywhere, Category = "Interaction|Physics")
	float PullForce = 1500.f;

	/** The maximum impulse applied to the object when it is being spit out */
	UPROPERTY(EditAnywhere, Category = "Interaction|Physics")
	float MaxLaunchImpulse = 2000.f;

	/** The maximum time the player can charge before swallowing */
	UPROPERTY(EditAnywhere, Category = "Interaction|Physics")
	float MaxChargeTime = 1.5f;

	UPROPERTY(VisibleAnywhere, Category = "Interaction|Detection")
	TObjectPtr<USphereComponent> DetectionSphere;

	UPROPERTY()
	TArray<TWeakObjectPtr<AActor>> Candidates;

	UFUNCTION()
	void OnDetectionBeginOverlap(UPrimitiveComponent* OverlappedComp, AActor* OtherActor,
		UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& Sweep);

	UFUNCTION()
	void OnDetectionEndOverlap(UPrimitiveComponent* OverlappedComp, AActor* OtherActor,
		UPrimitiveComponent* OtherComp, int32 OtherBodyIndex);

public:
	/** Returns whether the object is currently being swallowed */
	bool IsSwallowing() const { return bIsSwallowing; }
	/** Returns whether the object is currently being spit out */
	bool IsSpitOut() const { return bIsSpitOut; }

	/** Starts the swallowing process */
	UFUNCTION(BlueprintCallable, Category = "Interaction")
	void StartSwallowing();

	/** Starts the spit out process */
	UFUNCTION(BlueprintCallable, Category = "Interaction")
	void StartSpitOut();

private:
	/** Whether the object is currently being swallowed */
	UPROPERTY(Category = "Interaction")
	bool bIsSwallowing = false;

	/** Whether the object is currently being spit out */
	UPROPERTY(Category = "Interaction")
	bool bIsSpitOut = false;
};
