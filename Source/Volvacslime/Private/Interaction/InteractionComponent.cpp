// Fill out your copyright notice in the Description page of Project Settings.

#include "Interaction/InteractionComponent.h"
#include "Interaction/Interactable.h"

#include "Engine/World.h"

UInteractionComponent::UInteractionComponent()
{
	PrimaryComponentTick.bCanEverTick = false;
}

void UInteractionComponent::StartSwallowing()
{
	UWorld* World = GetWorld();
	if (!World)
		return;

	FHitResult HitResult;
	bool bHit = World->LineTraceSingleByChannel(HitResult, GetOwner()->GetActorLocation(), GetOwner()->GetActorLocation() + FVector(0, 0, -100), CollisionChannel);

	if (bHit && HitResult.GetActor() && HitResult.GetActor()->GetClass()->ImplementsInterface(UInteractable::StaticClass()))
	{
		bIsSwallowing = true;
	};

	return;
}

void UInteractionComponent::StartSpitOut()
{
	bIsSpitOut = true;
}